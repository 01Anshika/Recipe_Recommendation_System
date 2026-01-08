from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Recipe
from .forms import IngredientSelectionForm

# YouTube API
from googleapiclient.discovery import build

# Primary recipes mapping
PRIMARY_RECIPES = {
    "rice": "Plain Rice",
    "tomato": "Tomato Chutney",
    "egg": "Boiled Egg",
    "potato": "Boiled Potato",
    "chicken": "Grilled Chicken",
    "paneer": "Paneer Cubes",
    "milk": "Milkshake",
    "chana dal": "Boiled Chana Dal",
    "moong dal": "Moong Dal Soup",
    "masoor dal": "Masoor Dal Soup",
    "rajma": "Boiled Rajma",
    "chole": "Chole Curry",
    "pasta": "Boiled Pasta",
    "noodles": "Boiled Noodles",
    "bread": "Plain Toast",
    "sooji": "Suji Halwa",
    "wheat flour": "Chapati",
    "cauliflower": "Boiled Cauliflower",
    "cabbage": "Boiled Cabbage",
    "capsicum": "Stir-fried Capsicum",
    "peas": "Boiled Peas",
    "carrot": "Boiled Carrot",
    "spinach": "Palak Curry",
    "corn": "Boiled Corn",
    "mushroom": "Sauteed Mushroom",
    "brinjal": "Baingan Bharta",
    "beans": "Boiled Beans",
    "ladyfinger": "Bhindi Fry",
    "bottle gourd": "Lauki Curry",
    "fish": "Grilled Fish"
}

def home(request):
    return render(request, 'recipe/index.html')

def register_view(request):
    error = None
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password = (request.POST.get('password') or '').strip()

        if not username or not password:
            error = 'Username and password required'
        elif User.objects.filter(username=username).exists():
            error = 'Username already exists'
        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')

    return render(request, 'recipe/register.html', {'error': error})

def login_view(request):
    error = None
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        password = (request.POST.get('password') or '').strip()

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('ingredient_select')
        else:
            error = 'Invalid credentials'

    return render(request, 'recipe/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def ingredient_select(request):
    if request.method == 'POST':
        form = IngredientSelectionForm(request.POST)
        print("POST DATA:", request.POST)
        if form.is_valid():
            print("FORM VALID? True")
            request.session['ingredients'] = form.cleaned_data['ingredients']
            request.session['servings'] = form.cleaned_data['servings']
            request.session['meal_type'] = form.cleaned_data['meal_type']
            print("Session updated:", request.session['ingredients'])
            return redirect('results')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = IngredientSelectionForm()

    return render(request, 'recipe/ingredient_select.html', {'form': form})

@login_required
def results(request):
    selected_ingredients = request.session.get('ingredients', [])
    print("Selected Ingredients (session):", selected_ingredients)

    if isinstance(selected_ingredients, str):
        selected_ingredients = [i.strip() for i in selected_ingredients.split(',')]
    selected_ingredients_lc = [ing.lower() for ing in selected_ingredients]

    servings = request.session.get('servings', 1)
    meal_type = request.session.get('meal_type', 'Dinner')

    results_list = []

    YOUTUBE_API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your API key

    if selected_ingredients_lc:
        all_recipes = list(Recipe.objects.all())

        # Primary recipes
        primary_recipes = []
        for ing in selected_ingredients_lc:
            primary_name = PRIMARY_RECIPES.get(ing)
            if primary_name:
                primary_recipes += [r for r in all_recipes if r.name.lower() == primary_name.lower()]

        # Common recipes (all selected ingredients)
        common_recipes = []
        for r in all_recipes:
            r_ingredients = [i.lower().strip() for i in r.clean_ingredients]
            if all(ing in r_ingredients for ing in selected_ingredients_lc) and r not in primary_recipes:
                common_recipes.append(r)

        # Individual recipes (any selected ingredient)
        individual_recipes = []
        for r in all_recipes:
            r_ingredients = [i.lower().strip() for i in r.clean_ingredients]
            if any(ing in r_ingredients for ing in selected_ingredients_lc) and r not in primary_recipes + common_recipes:
                individual_recipes.append(r)

        final_recipes = primary_recipes + common_recipes + individual_recipes

        # YouTube API
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

        for r in final_recipes:
            youtube_url = None
            try:
                request_youtube = youtube.search().list(
                    part="snippet",
                    q=r.name,
                    type="video",
                    maxResults=1
                )
                response = request_youtube.execute()
                if response['items']:
                    video_id = response['items'][0]['id']['videoId']
                    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            except:
                youtube_url = None

            if r in primary_recipes:
                r_type = 'primary'
            elif r in common_recipes:
                r_type = 'common'
            else:
                r_type = 'individual'

            results_list.append({
                'recipe': r,
                'ingredients_list': r.clean_ingredients,
                'instructions': r.instructions or "Instructions not available.",
                'cooking_time': r.cook_time,
                'youtube': youtube_url or f"https://www.youtube.com/results?search_query={r.name}",
                'type': r_type
            })

    return render(request, 'recipe/results.html', {'results': results_list})

@login_required
def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
