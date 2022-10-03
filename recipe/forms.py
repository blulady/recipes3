from django.forms import ModelForm
from .models import Recipe


class CreateRecipeModelForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'diet', 'cook_time', 'chef', 'directions', 'difficulty_level', 'ingredients',
                  'associated_recipe', 'origin']
        help_texts = {'title': _('Name of the Recipe'), 'diet': _('Type of diet(s) this recipe falls under'),
                      'cook_time': _("Both prep and cook time"), "chef": _('Your User Name'),
                      "directions": _("cooking and prepping instructions"),
                      'ingredients': _("add ingredients and measurements"),
                      "associated_recipe": _("does this recipe require another recipe (dressing, icing"),
                      'origin': _("credit your source (website, book, author)")}
