from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized
import unittest
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
        response = self.client.get(reverse('recipes')+ '?page=2')
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
        response = self.client.get(reverse('diets')+'?page=2')
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

        test_recipe = Recipe.objects.create(title='Mediterranean Salad Dressing', cook_time='an hour and a half',
                              directions="a string that acts as instructions as to how to cook the dish",
                              difficulty_level="Difficult", ingredients="another string that acts as ingredients",
                              origin="aunt mary")
        test_diet = Diet.objects.create('Vegan')
