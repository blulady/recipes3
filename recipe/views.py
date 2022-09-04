from django.shortcuts import render
from .models import Diet, Ingredients, Recipe
from django.views import generic


def index(request):
    """view function for home page of site"""
    recipe_count = Recipe.objects.all().count()
    diet_count = Diet.objects.all().count()

    context = {
        'recipe_count': recipe_count,
        'diet_count': diet_count
    }

    return render(request, 'index.html', context=context)


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 10


class RecipeDetailView(generic.DetailView):
    model = Recipe
