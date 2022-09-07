from django.shortcuts import render
from .models import Diet, Ingredients, Recipe
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


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


class RecipeByUserListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'recipe/recipe_list_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Recipe.objects.filter(who_entered=self.request.user).order_by('title')


class DietListView(generic.ListView):
    model = Diet
    paginate_by = 10


class DietDetailView(generic.DetailView):
    model = Diet
    
