from django import forms

class IngredientSelectionForm(forms.Form):
    INGREDIENT_CHOICES = [
        ('rice', 'Rice'), ('wheat flour', 'Wheat Flour'), ('sooji', 'Sooji/Semolina'),
        ('oats', 'Oats'), ('poha', 'Poha'), ('maida', 'Maida'), ('milk', 'Milk'),
        ('paneer', 'Paneer'), ('curd', 'Curd'), ('potato', 'Potato'), ('cauliflower', 'Cauliflower/Gobi'),
        ('cabbage', 'Cabbage'), ('capsicum', 'Capsicum'), ('peas', 'Peas'), ('carrot', 'Carrot'),
        ('tomato', 'Tomato'), ('spinach', 'Spinach/Palak'), ('corn', 'Corn'), ('mushroom', 'Mushroom'),
        ('brinjal', 'Brinjal/Baingan'), ('beans', 'Beans'), ('ladyfinger', 'Ladyfinger/Bhindi'),
        ('bottle gourd', 'Bottle Gourd/Lauki'), ('egg', 'Egg'), ('chicken', 'Chicken'), ('fish', 'Fish'),
        ('chana dal', 'Chana Dal'), ('moong dal', 'Moong Dal'), ('masoor dal', 'Masoor Dal'),
        ('rajma', 'Rajma'), ('chole', 'Chole'), ('pasta', 'Pasta'), ('noodles', 'Noodles'),
        ('bread', 'Bread')
    ]

    ingredients = forms.MultipleChoiceField(
        choices=INGREDIENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Ingredients"
    )

    servings = forms.IntegerField(
        min_value=1,
        initial=2,
        required=True,
        label="Number of Servings"
    )

    meal_type = forms.ChoiceField(
        choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')],
        initial='dinner',
        required=True,
        label="Meal Type"
    )
