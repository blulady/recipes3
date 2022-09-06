from django.contrib import admin
from .models import Diet, Ingredients, Recipe

admin.site. register(Diet)
admin.site.register(Ingredients)
admin.site.register(Recipe)

# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'who_entered', 'diet')



