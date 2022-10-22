from django.test import TestCase

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
        self.assertTrue(form.fields['field_name'].label is None or form.fields['field_name'].label == 'field_label')e your tests here.
