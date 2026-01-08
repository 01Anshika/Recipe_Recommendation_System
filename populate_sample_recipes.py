# populate_sample_recipes.py
from recipe.models import Recipe

# wipe old recipes
Recipe.objects.all().delete()

MAIN_INGREDIENTS = [
    "rice", "wheat flour", "sooji", "semolina", "oats", "poha", "maida",
    "milk", "paneer", "curd", "potato", "cauliflower", "cabbage", "capsicum",
    "peas", "carrot", "tomato", "spinach", "corn", "mushroom", "brinjal",
    "beans", "ladyfinger", "bottle gourd", "egg", "chicken", "fish",
    "chana dal", "moong dal", "masoor dal", "rajma", "chole", "pasta",
    "noodles", "bread"
]

# ---------------- PRIMARY (one per main ingredient) ----------------
primary_recipes = [
    {"name": "Plain Rice", "ingredients": ["rice"], "instructions": "Boil rice in water until soft."},
    {"name": "Chapati (Wheat Flour Roti)", "ingredients": ["wheat flour"], "instructions": "Knead wheat flour with water, roll and cook on tawa."},
    {"name": "Suji (Soji) Halwa", "ingredients": ["sooji"], "instructions": "Roast sooji in ghee, add milk/sugar and cook to halwa consistency."},
    {"name": "Semolina Porridge", "ingredients": ["semolina"], "instructions": "Cook semolina with milk/water and sugar to make porridge."},
    {"name": "Oats Porridge", "ingredients": ["oats"], "instructions": "Cook oats with water or milk until soft."},
    {"name": "Poha (Flattened Rice)", "ingredients": ["poha"], "instructions": "Rinse poha and cook with light tempering of mustard, curry leaves and peanuts."},
    {"name": "Maida Flatbread / Basic dough", "ingredients": ["maida"], "instructions": "Use maida for basic dough and breads."},
    {"name": "Glass of Milk", "ingredients": ["milk"], "instructions": "Boil milk and serve warm or chilled."},
    {"name": "Paneer Cubes", "ingredients": ["paneer"], "instructions": "Cut paneer into cubes and lightly sauté or use directly."},
    {"name": "Curd Bowl", "ingredients": ["curd"], "instructions": "Serve fresh curd or use for raita."},
    {"name": "Boiled Potato", "ingredients": ["potato"], "instructions": "Boil potatoes until tender."},
    {"name": "Cauliflower Roast", "ingredients": ["cauliflower"], "instructions": "Roast or sauté cauliflower with simple spices."},
    {"name": "Cabbage Salad", "ingredients": ["cabbage"], "instructions": "Shred cabbage and serve raw or lightly sauté."},
    {"name": "Capsicum Stir-Fry", "ingredients": ["capsicum"], "instructions": "Slice and quickly stir-fry capsicum."},
    {"name": "Peas (Boiled/Steamed)", "ingredients": ["peas"], "instructions": "Boil peas until tender; use in pulao or curry."},
    {"name": "Carrot Snack", "ingredients": ["carrot"], "instructions": "Grate or boil carrot and use in salads or cooking."},
    {"name": "Tomato Chutney", "ingredients": ["tomato"], "instructions": "Cook tomatoes with seasoning to make chutney or base."},
    {"name": "Spinach Soup", "ingredients": ["spinach"], "instructions": "Cook spinach and blend into a soup or make palak base."},
    {"name": "Boiled Corn", "ingredients": ["corn"], "instructions": "Boil corn and serve with butter or salt."},
    {"name": "Mushroom Sauté", "ingredients": ["mushroom"], "instructions": "Sauté mushrooms with garlic and butter."},
    {"name": "Brinjal (Baingan) Roast", "ingredients": ["brinjal"], "instructions": "Cook brinjal with spices or roast whole and mash."},
    {"name": "Stir-Fried Beans", "ingredients": ["beans"], "instructions": "Stir-fry beans with basic spices."},
    {"name": "Bhindi Fry (Ladyfinger)", "ingredients": ["ladyfinger"], "instructions": "Fry ladyfinger with spices."},
    {"name": "Bottle Gourd Curry", "ingredients": ["bottle gourd"], "instructions": "Cook bottle gourd into a light curry."},
    {"name": "Boiled Egg", "ingredients": ["egg"], "instructions": "Boil egg for 8-10 minutes; serve sliced or whole."},
    {"name": "Grilled Chicken", "ingredients": ["chicken"], "instructions": "Grill or pan-fry chicken with salt and simple spices."},
    {"name": "Fried Fish", "ingredients": ["fish"], "instructions": "Marinate and fry fish fillets."},
    {"name": "Chana Dal Tadka", "ingredients": ["chana dal"], "instructions": "Cook chana dal and temper with spices."},
    {"name": "Moong Dal Soup", "ingredients": ["moong dal"], "instructions": "Cook moong dal into a light soup/khichdi base."},
    {"name": "Masoor Dal", "ingredients": ["masoor dal"], "instructions": "Cook masoor dal with simple tadka."},
    {"name": "Rajma Simple Curry", "ingredients": ["rajma"], "instructions": "Soak and cook rajma with spices."},
    {"name": "Chole Basic", "ingredients": ["chole"], "instructions": "Soak and cook chole with basic spices."},
    {"name": "Plain Pasta", "ingredients": ["pasta"], "instructions": "Boil pasta and toss with basic sauce or oil."},
    {"name": "Boiled Noodles", "ingredients": ["noodles"], "instructions": "Boil noodles; use as base for stir-fry."},
    {"name": "Bread Slice", "ingredients": ["bread"], "instructions": "Toast or use bread slices."},
]

# ---------------- SECONDARY (realistic multi-ingredient recipes) ----------------
secondary_recipes = [
    # Rice-based
    {"name": "Vegetable Fried Rice", "ingredients": ["rice", "carrot", "peas", "capsicum"], "instructions": "Stir-fry cooked rice with mixed vegetables and soy/seasoning."},
    {"name": "Peas Pulao", "ingredients": ["rice", "peas"], "instructions": "Cook rice with peas and mild spices."},
    {"name": "Tomato Rice", "ingredients": ["rice", "tomato"], "instructions": "Cook rice with tomato puree and mild spices."},
    {"name": "Curd Rice", "ingredients": ["rice", "curd"], "instructions": "Mix cooked rice with curd and tempering."},

    # Wheat flour based
    {"name": "Aloo Paratha", "ingredients": ["wheat flour", "potato"], "instructions": "Mix wheat flour dough, stuff with spiced mashed potato and cook."},
    {"name": "Chapati", "ingredients": ["wheat flour"], "instructions": "Make and cook chapatis on tawa."},

    # Sooji / semolina
    {"name": "Suji Halwa (Sweet)", "ingredients": ["sooji", "milk"], "instructions": "Roast sooji in ghee, add milk and sugar, cook until thick."},
    {"name": "Semolina Upma", "ingredients": ["semolina", "vegetables"], "instructions": "Toast semolina and cook with vegetables and seasoning."},

    # Oats / breakfast
    {"name": "Oats Porridge with Milk", "ingredients": ["oats", "milk"], "instructions": "Cook oats in milk until creamy; add sugar or salt as desired."},

    # Poha
    {"name": "Kanda Poha (Spiced Poha)", "ingredients": ["poha", "onion", "peanut"], "instructions": "Rinse poha and cook with onion, mustard seeds and peanuts."},

    # Paneer
    {"name": "Paneer Butter Masala", "ingredients": ["paneer", "tomato", "milk"], "instructions": "Cook paneer in a tomato-based creamy gravy."},
    {"name": "Paneer Bhurji", "ingredients": ["paneer", "tomato", "capsicum"], "instructions": "Crumble paneer and sauté with onion, tomato and capsicum."},

    # Potato
    {"name": "Aloo Sabzi (Indian Potato Curry)", "ingredients": ["potato", "tomato"], "instructions": "Cook potatoes with tomato, turmeric and spices."},
    {"name": "Jeera Aloo", "ingredients": ["potato"], "instructions": "Fry boiled potato with cumin and mild spices."},

    # Cauliflower
    {"name": "Aloo Gobi", "ingredients": ["potato", "cauliflower", "tomato"], "instructions": "Cook potato and cauliflower together with spices."},

    # Cabbage
    {"name": "Cabbage Stir Fry", "ingredients": ["cabbage", "carrot"], "instructions": "Shred and stir fry cabbage with carrots and spices."},

    # Capsicum
    {"name": "Capsicum Stir-Fry with Paneer", "ingredients": ["capsicum", "paneer"], "instructions": "Sauté capsicum with paneer and spices."},

    # Peas & carrot
    {"name": "Vegetable Pulao (mixed)", "ingredients": ["rice", "peas", "carrot", "capsicum"], "instructions": "Cook rice with mixed vegetables and whole spices."},

    # Tomato-based
    {"name": "Tomato Soup", "ingredients": ["tomato", "milk"], "instructions": "Cook and blend tomatoes; add milk or cream to taste."},

    # Spinach
    {"name": "Palak (Spinach) Sauté", "ingredients": ["spinach", "garlic"], "instructions": "Sauté spinach with garlic and mild spices."},

    # Corn
    {"name": "Corn Salad", "ingredients": ["corn", "butter"], "instructions": "Boiled corn tossed in butter and salt."},

    # Mushroom
    {"name": "Mushroom Masala", "ingredients": ["mushroom", "tomato"], "instructions": "Cook mushroom in tomato-onion masala."},
    {"name": "Creamy Mushroom", "ingredients": ["mushroom", "milk"], "instructions": "Cook mushrooms in a creamy milk-based sauce."},

    # Brinjal
    {"name": "Baingan Bharta", "ingredients": ["brinjal", "tomato"], "instructions": "Roast brinjal, mash and cook with tomato and spices."},

    # Beans
    {"name": "Green Beans Stir Fry", "ingredients": ["beans", "carrot"], "instructions": "Stir-fry green beans with carrots and light seasoning."},

    # Ladyfinger
    {"name": "Bhindi Masala", "ingredients": ["ladyfinger", "tomato"], "instructions": "Cook ladyfinger with onions and tomato masala."},

    # Bottle gourd
    {"name": "Lauki Curry", "ingredients": ["bottle gourd", "tomato"], "instructions": "Cook bottle gourd in a light curry."},

    # Egg
    {"name": "Egg Curry", "ingredients": ["egg", "tomato"], "instructions": "Cook boiled eggs in a spicy tomato gravy."},
    {"name": "Egg Bhurji", "ingredients": ["egg", "onion", "tomato"], "instructions": "Scramble eggs with spices and vegetables."},

    # Chicken
    {"name": "Chicken Curry", "ingredients": ["chicken", "tomato"], "instructions": "Cook chicken in onion-tomato based gravy."},

    # Fish
    {"name": "Fish Curry", "ingredients": ["fish", "tomato"], "instructions": "Cook fish in a tangy tomato-based curry."},

    # Dals
    {"name": "Dal Tadka", "ingredients": ["moong dal", "masoor dal"], "instructions": "Cook dals and temper with ghee, cumin and garlic."},
    {"name": "Chana Dal Curry", "ingredients": ["chana dal", "tomato"], "instructions": "Cook chana dal with spices and tomato."},

    # Rajma & Chole
    {"name": "Rajma Masala", "ingredients": ["rajma", "tomato"], "instructions": "Cook rajma in onion-tomato gravy."},
    {"name": "Chole Masala", "ingredients": ["chole", "tomato"], "instructions": "Cook chole in a spicy masala."},

    # Pasta & noodles
    {"name": "Pasta with Tomato Sauce", "ingredients": ["pasta", "tomato"], "instructions": "Boil pasta and toss with tomato sauce."},
    {"name": "Veg Noodles", "ingredients": ["noodles", "carrot", "capsicum"], "instructions": "Stir-fry noodles with vegetables."},

    # Bread combos
    {"name": "Bread Sandwich", "ingredients": ["bread", "tomato", "cabbage"], "instructions": "Assemble bread with tomato, cabbage and chutney."},
]

# ---------------- COMMON (logical combos - flexible match: recipe must include all selected ingredients) ----------------
common_recipes = [
    {"name": "Tomato Rice", "ingredients": ["rice", "tomato"], "instructions": "Cook rice with tomato puree and mild spices."},
    {"name": "Vegetable Pulao", "ingredients": ["rice", "peas", "carrot", "capsicum"], "instructions": "Cook rice with mixed vegetables and whole spices."},
    {"name": "Paneer Butter Masala", "ingredients": ["paneer", "tomato", "milk"], "instructions": "Cook paneer in a creamy tomato-based gravy."},
    {"name": "Aloo Paratha", "ingredients": ["wheat flour", "potato"], "instructions": "Stuff wheat flour dough with spiced mashed potato and cook."},
    {"name": "Egg & Tomato Curry", "ingredients": ["egg", "tomato"], "instructions": "Boil eggs and cook in tomato-onion gravy."},
    {"name": "Palak Paneer", "ingredients": ["spinach", "paneer"], "instructions": "Cook paneer in a spinach-based gravy."},
    {"name": "Rice & Chicken Pulao", "ingredients": ["rice", "chicken"], "instructions": "Cook rice with chicken and mild spices."},
    {"name": "Masala Dosa with Potato Filling", "ingredients": ["rice", "potato"], "instructions": "Prepare dosa batter with rice and stuff with potato masala."},
    {"name": "Rajma Chawal", "ingredients": ["rajma", "rice"], "instructions": "Serve rajma curry with plain rice."},
    {"name": "Chole Bhature (simple)", "ingredients": ["chole", "wheat flour"], "instructions": "Cook chole and serve with bread made from wheat flour."},
    {"name": "Pasta Tomato Basil", "ingredients": ["pasta", "tomato"], "instructions": "Boil pasta and toss with tomato and herbs."},
    {"name": "Vegetable Noodles", "ingredients": ["noodles", "carrot", "capsicum"], "instructions": "Stir-fry noodles with mixed vegetables."},
    {"name": "Egg Sandwich", "ingredients": ["egg", "bread"], "instructions": "Make sandwich with boiled egg and bread slices."},
    {"name": "Suji Porridge with Milk", "ingredients": ["sooji", "milk"], "instructions": "Cook sooji in milk with sugar to make porridge."},
    {"name": "Mushroom Tomato Curry", "ingredients": ["mushroom", "tomato"], "instructions": "Cook mushrooms in a rich tomato gravy."},
]

# ---------------- Insert everything into DB ----------------
all_recipes = primary_recipes + secondary_recipes + common_recipes

for r in all_recipes:
    Recipe.objects.create(name=r["name"], ingredients=r["ingredients"], instructions=r["instructions"])

print(f"Inserted {len(all_recipes)} recipes into the database.")
