#!/use/bin/env python3

# Create a string variable over multi line

recipe_instruction = """Preheat oven to 350°F (175°C).
In a bowl, mix 2 cups flour, 1 cup sugar, and 1 tsp salt.
Add 2 eggs and 1 cup milk; stir until smooth.
Pour batter into a greased pan.
Bake for 25–30 minutes or until golden brown.
Let cool before serving."""

recipe_instruction_2 = (
    "Preheat oven to 350°F (175°C).\n"
    "In a bowl, mix 2 cups flour, 1 cup sugar, and 1 tsp salt.\n"
    "Add 2 eggs and 1 cup milk; stir until smooth.\n"
    "Pour batter into a greased pan.\n"
    "Bake for 25–30 minutes or until golden brown.\n"
    "Let cool before serving."
)

print(recipe_instruction)
print("\n")
print(recipe_instruction_2)

# Methods available in string
# 1. Replace
s = "2 cups, 1 cup"
print(s.replace("cup", "cup(s)"))  # -> "2 cup(s)s, 1 cup(s)"  (bad)


# 2. lower
pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)
