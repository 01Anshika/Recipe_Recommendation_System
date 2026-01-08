from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.JSONField(default=list)
    instructions = models.TextField(blank=True)
    cook_time_minutes = models.PositiveIntegerField(default=30)
    servings = models.PositiveIntegerField(default=2)
    meal_type = models.CharField(
        max_length=50,
        choices=[
            ('breakfast','Breakfast'),
            ('lunch','Lunch'),
            ('dinner','Dinner'),
            ('snack','Snack')
        ],
        default='dinner'
    )
    youtube_query = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def cook_time(self):
        return self.cook_time_minutes

    @property
    def clean_ingredients(self):
        return [str(i).strip().lower() for i in self.ingredients]
