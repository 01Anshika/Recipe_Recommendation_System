from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # home page
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('select/', views.ingredient_select, name='ingredient_select'),
    path('results/', views.results, name='results'),
    path('recipe/<int:recipe_id>/', views.recipe_detail_view, name='recipe_detail'),
    ]
