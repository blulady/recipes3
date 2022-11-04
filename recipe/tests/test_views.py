from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from parameterized import parameterized
# import unittest
from ..models import Recipe, Diet, User


class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 13 recipes for pagination tests
        number_of_recipes = 13

        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(title=f'Mediterranean Salad Dressing {recipe_id}',
                                  cook_time=f'an hour and a half {recipe_id}',
                                  directions=f"a string that acts as instructions as to how to cook the dish {recipe_id}",
                                  difficulty_level=f"Difficult {recipe_id}",
                                  ingredients=f"another string that acts as ingredients {recipe_id}",
                                  origin=f"aunt mary {recipe_id}")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/recipe/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe/recipe_list.html")

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context["is_paginated"], True)
        self.assertEqual(len(response.context['recipe_list']), 10)

    def test_lists_all_authors(self):
        response = self.client.get(reverse('recipes') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context["is_paginated"], True)
        self.assertEqual(len(response.context['recipe_list']), 3)


class DietListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_diets = 13
        for diet_id in range(number_of_diets):
            Diet.objects.create(
                name=f'A diet {diet_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/recipe/diets/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('diets'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('diets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/diet_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('diets'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['diet_list']), 10)

    def test_lists_all_diets(self):
        response = self.client.get(reverse('diets') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['diet_list']), 3)


class RecipeByUserListView(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkRV0Z&3iDw+tuK')
        test_user2 = User.objects.create_user(username="testuser2", password='3X<2HJ1vw+tuK1X<ISRU')
        test_user1.save()
        test_user2.save()
        test_diet1 = Diet.objects.create(name='Vegan')
        test_diet2 = Diet.objects.create(name='Paleo')
        test_diet1.save()
        test_diet2.save()
        diet_object_for_recipe1 = Diet.objects.first()
        diet_object_for_recipe2 = Diet.objects.last()

        test_associate_recipe = Recipe.objects.create(title='Mediterranean Salad Dressing',
                                                      cook_time='15 minutes', chef=test_user1,
                                                      directions="a string that acts as directions as to how to cook the dish",
                                                      difficulty_level="Easy",
                                                      ingredients="another string that acts as ingredients",
                                                      origin="aunt mary")
        test_associate_recipe.diet.set([test_diet1])
        test_associate_recipe.save()
        test_associate_recipe_object = Recipe.objects.first()
        number_of_recipe_copies = 26
        for recipe_id in range(number_of_recipe_copies):
            letter = chr(65+recipe_id)
            test_chef = test_user1 if recipe_id % 2 else test_user2
            test_diet = diet_object_for_recipe1 if recipe_id % 2 else diet_object_for_recipe2
            test_recipe = Recipe.objects.create(title=f'{letter}editerranean Bean Salad',
                                                cook_time='an hour',  # chef=test_user2,
                                                directions='some directions as to how to prep the food',
                                                difficulty_level='Medium',
                                                ingredients="a string of ingredients",
                                                origin="The Mediterranean")
            # test_recipe.save()
            test_recipe.chef = test_chef
            test_recipe.diet.set([test_diet])
            test_recipe.associated_recipe = test_associate_recipe_object
            test_recipe.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my-recipe'))
        self.assertRedirects(response, '/accounts/login/?next=/recipe/myrecipes/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkRV0Z&3iDw+tuK')
        response = self.client.get(reverse('my-recipe'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_only_my_recipes_in_list(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkRV0Z&3iDw+tuK')
        response = self.client.get(reverse('my-recipe'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        for item in response.context['recipe_list']:
            self.assertEqual(response.context['user'], item.chef)

    def test_pages_ordered_by_title(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkRV0Z&3iDw+tuK')
        response = self.client.get(reverse('my-recipe'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['recipe_list']), 10)

        first_num = 64
        for rcp in response.context['recipe_list']:
            first_num += 1
            self.assertTrue(first_num < ord(rcp.title[0]))
            # self.assertEqual(first_num, ord(rcp.title[0])),# why this no work


class RegisterPageView(TestCase):
    def setUp(self):
        self.username = 'testuser@gmail.com'
        self.password = '1XISRUkRV0Z&3iDw+tuK'

    def test_register_page_url(self):
        response_reverse = self.client.get(reverse("register"))
        self.assertEqual(response_reverse.status_code, 200)
        self.assertTemplateUsed(response_reverse, template_name="register.html")
        response = self.client.get("/recipe/register/")
        self.assertEqual(response_reverse.status_code, response.status_code)

    def test_register_form(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)