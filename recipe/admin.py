# recipe/admin.py
from django.contrib import admin
from .models import Recipe

# Recipe model ko admin me register karna
admin.site.register(Recipe)
