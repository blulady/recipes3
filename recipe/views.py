from django.shortcuts import render
from .models import Diet, Recipe
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateRecipeModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


# @login_required
# def create_recipe(request, pk):
#     """View function for creating a recipe by a user"""
#     new_recipe = get_object_or_404(Recipe, pk=pk)
#     # if this is a post request then process the form data
#     if request.method == 'POST':
#         # create a form instance & populated it w/date from the request binding
#         form = CreateRecipeModelForm(request.POST)
#         # check if the form is valid
#         if form.is_valid():
#             # process the data in form.cleaned data as required
#             # might need to confirm User is an actual User
#             new_recipe.save()
#             return HttpResponseRedirect(reverse('recipe-detail'))
#         else:
#             context = {
#                 'form': form,
#                 'new_recipe': new_recipe
#             }
#             return render(request, 'recipe/recipe_create_new.html', context)
#LoginRequiredMixin,

class AuthorCreate(CreateView, LoginRequiredMixin):
    model = Recipe
    fields = ['title', 'diet', 'cook_time', 'chef', 'directions', 'difficulty_level',
              'ingredients', 'associated_recipe', 'origin']
    template_name_suffix = '_create_new'