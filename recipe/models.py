from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Diet(models.Model):
    name = models.CharField(max_length=200, help_text='Type of diet')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        """returns url to access a detail record for a recipe"""
        return reverse("diet-detail", args=[str(self.id)])


class Recipe(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=250, help_text='Title of Recipe')
    who_entered = models.CharField(max_length=100, help_text="user name", blank=True, null=True)
    diet = models.ManyToManyField(Diet, blank=True)
    cook_time = models.CharField(max_length=50, help_text='total cooking time')
    chef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    directions = models.TextField()
    LEVEL = (
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Difficult", "Difficult"),
        ("Extremely Difficult", "Extremely Difficult")
    )
    difficulty_level = models.CharField(
        max_length=20,
        choices=LEVEL,
        blank=False,
        help_text="What level of skill does this recipe require?"
    )
    ingredients = models.TextField()
    associated_recipe = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    origin = models.CharField(max_length=250, help_text="is there a source you'd like to cite for this recipe? "
                                                        "Enter a book name or link here")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """returns url to access a detail record for a recipe"""
        return reverse("recipe-detail", args=[str(self.id)])


