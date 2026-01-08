import os
import django

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from recipe.models import Recipe

# 20 recipes with English instructions
instructions_data = {
    "Tomato Pasta": """1. Boil the pasta for 8-10 minutes.
2. Heat some oil in a pan and sauté garlic and onion.
3. Add tomato puree and cook for 5 minutes.
4. Add salt, chilli flakes, oregano, and black pepper.
5. Add the boiled pasta and mix well.
6. Cook for 2 minutes and serve hot.""",

    "Veg Sandwich": """1. Take 2 slices of bread.
2. Spread butter on one slice and green chutney on the other.
3. Add cucumber, tomato, and onion slices.
4. Sprinkle salt and pepper.
5. Close both slices and grill/toast.
6. Cut and serve the sandwich.""",

    "Chicken Curry": """1. Wash the chicken and marinate with salt, turmeric, chili, and yogurt.
2. Heat oil and fry onions until golden.
3. Add tomato and garlic-ginger paste, sauté the masala.
4. Add marinated chicken and cook for 10 minutes.
5. Add water and cook for 20-25 minutes.
6. Garnish with fresh coriander and serve.""",

    "Pancakes": """1. Mix flour, sugar, baking powder, and salt in a bowl.
2. In a separate bowl, whisk milk, egg, and melted butter.
3. Combine both mixtures.
4. Heat a pan and add a little butter.
5. Pour the batter and cook until bubbles appear.
6. Flip and cook until golden, then serve.""",

    "Grilled Cheese": """1. Spread butter on bread slices.
2. Place cheese slices on one slice.
3. Cover with the other slice to make a sandwich.
4. Grill in a pan until both sides are golden.
5. Serve hot.""",

    "Veg Biryani": """1. Boil basmati rice till 70% cooked.
2. Fry vegetables in oil.
3. Mix curd, biryani masala, salt, and fried onions.
4. Layer rice and vegetable mixture alternately.
5. Cook on dum for 15 minutes.
6. Serve with raita.""",

    "Omelette": """1. Break 2 eggs into a bowl.
2. Add salt, onion, and green chili.
3. Heat oil in a pan.
4. Pour the egg mixture and cook on medium flame.
5. Flip and cook both sides until golden.
6. Serve.""",

    "Fruit Salad": """1. Cut apple, banana, grapes, papaya, and mango into pieces.
2. Mix all fruits in a bowl.
3. Add a little honey or chaat masala.
4. Serve.""",

    "Spaghetti": """1. Boil the spaghetti.
2. Sauté garlic and onion in a pan.
3. Add tomato sauce.
4. Add salt, pepper, and oregano.
5. Mix in boiled spaghetti.
6. Serve.""",

    "Chicken Sandwich": """1. Shred chicken and mix with mayo.
2. Add salt, pepper, and onion.
3. Spread mixture on bread.
4. Grill the sandwich.
5. Serve.""",

    "Masala Dosa": """1. Spread dosa batter on a tawa.
2. Place potato masala in the center.
3. Fold the dosa.
4. Serve with coconut chutney and sambar.""",

    "Paneer Butter Masala": """1. Heat butter and cook onion and tomatoes.
2. Make puree and return to pan.
3. Add salt, chili, and garam masala.
4. Add paneer cubes.
5. Add cream and cook for 5 minutes.
6. Serve.""",

    "Veg Soup": """1. Chop vegetables.
2. Heat butter in a pan and sauté vegetables.
3. Add water and boil for 10 minutes.
4. Add salt and pepper.
5. Serve.""",

    "Fried Rice": """1. Boil rice till 80% cooked.
2. Fry vegetables in oil.
3. Add salt, soy sauce, and pepper.
4. Add rice and stir-fry on high flame.
5. Serve.""",

    "Chocolate Cake": """1. Mix flour, cocoa powder, and sugar in a bowl.
2. Add milk, oil, and vanilla.
3. Pour batter into a tin.
4. Bake for 30-35 minutes.
5. Decorate with chocolate syrup.""",

    "Egg Curry": """1. Boil the eggs.
2. Prepare onion, tomato, and garlic masala.
3. Add spices and fry.
4. Add water.
5. Add eggs and simmer for 10 minutes.
6. Serve.""",

    "Aloo Paratha": """1. Boil the potatoes.
2. Mix the spices.
3. Make the dough.
4. Fill the stuffing.
5. Cook the paratha.
6. Serve.""",

    "Grilled Chicken": """1. Marinate chicken with spices, lemon, and yogurt.
2. Heat grill pan and cook.
3. Cook both sides until golden.
4. Serve.""",

    "Caesar Salad": """1. Chop the lettuce.
2. Add croutons.
3. Add Caesar dressing.
4. Add chicken or vegetables.
5. Toss and serve.""",

    "Maggie": """1. Boil water.
2. Add Maggie noodles.
3. Add the seasoning.
4. Cook for 2 minutes and serve."""
}

# Update recipes in DB
for name, instr in instructions_data.items():
    try:
        recipe = Recipe.objects.get(name=name)
        recipe.instructions = instr
        recipe.save()
        print(f"{name} → Instructions Updated in English")
    except Recipe.DoesNotExist:
        print(f"{name} NOT FOUND in DB")
