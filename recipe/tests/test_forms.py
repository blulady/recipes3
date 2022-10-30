from django.test import TestCase
from ..forms import CreateRecipeModelForm
from parameterized import parameterized
import unittest


class CreateRecipeModelFormTest(TestCase, unittest.TestCase):
    @parameterized.expand([
        ["title_label", 'title', 'Title'],
        ['diet_label', 'diet', 'Diet'],
        ['cook_time_label', 'cook_time', 'Cook time'],
        ['directions_label', 'directions', "Directions"],
        ['difficulty_level_label', 'difficulty_level', "Difficulty level"],
        ['ingredients_label', 'ingredients', 'Ingredients'],
        ["associated_recipe_label", 'associated_recipe', "Associated recipe"],
    ])
    def test_recipe_create_fields_label(self, test_name, field_name, field_label):
        form = CreateRecipeModelForm()
        self.assertTrue(form.fields[field_name].label is None or form.fields[field_name].label == field_label)

    @parameterized.expand([
        ["title_help_txt", "title",'Name of the Recipe'],
        ["diet_help_txt", "diet", 'Type of diet(s) this recipe falls under'],
        ["cook_time_help_txt", "cook_time", "Both prep and cook time"],
        ["directions_help_txt", "directions", "cooking and prepping instructions"],
        ["ingredients_help_txt", "ingredients", "add ingredients and measurements"],
        ["associated_recipe_help_txt", "associated_recipe", "does this recipe require another recipe (dressing, icing"],
        ["origin_help_txt", "origin", "credit your source (website, book, author)"]
    ])
    def test_recipe_create_help_text(self,test_name, field_label, help_txt):
        form = CreateRecipeModelForm()
        self.assertEqual(form.fields[field_label].help_text, help_txt)
