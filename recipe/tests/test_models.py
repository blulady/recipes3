from django.test import TestCase
from ..models import Diet, Recipe
from parameterized import parameterized
import unittest


class DietModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Diet.objects.create(name='Keto')

    def test_first_name_label(self):
        diet = Diet.objects.get(id=1)
        field_label = diet._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        diet = Diet.objects.get(id=1)
        max_length = diet._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        diet = Diet.objects.get(id=1)
        self.assertEqual(diet.get_absolute_url(), '/recipe/diet/1')

    def test_object_name_is_name(self):
        diet = Diet.objects.get(id=1)
        expect_object_name = f'{diet.name}'
        self.assertEqual(str(diet), expect_object_name)


class RecipeModelTest(TestCase, unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(title='Mediterranean Salad Dressing', cook_time='an hour and a half',
                              directions="a string that acts as instructions as to how to cook the dish",
                              difficulty_level="Difficult", ingredients="another string that acts as ingredients",
                              origin="aunt mary")

    @parameterized.expand([
        ["diet_label", "diet", "diet"],
        ["who_entered_label", "who_entered", 'who entered'],
        ['cook_time_label', 'cook_time', 'cook time'],
        ['title_label', 'title', 'title'],
        ['directions_label', 'directions', "directions"],
        ['ingredients_label', 'ingredients', 'ingredients'],
        ['origin_label', 'origin', 'origin']
    ])
    def test_label(self, name, a, b):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field(a).verbose_name
        self.assertEqual(field_label, b)

    @parameterized.expand([
        ['title_length', 'title', 250],
        ['who_entered_length', 'who_entered', 100],
        ['cook_title_length', "cook_time", 50],
        ['difficulty_level_length', 'difficulty_level', 20],
        ["origin_field", "origin", 250 ]
    ])
    def test_title_max_length(self, name, field, length):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field(field).max_length
        self.assertEqual(max_length, length)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipe/recipe/1')

    def test_name_is_name(self):



