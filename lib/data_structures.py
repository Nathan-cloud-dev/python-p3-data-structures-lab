spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return (names)
#get_names(spicy_foods)
def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods
    
#get_spiciest_foods(spicy_foods)
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
#print_spicy_foods(spicy_foods)
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return (food)
#get_spicy_food_by_cuisine(spicy_foods, "American")
def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    heat_levels = [food['heat_level'] for food in spicy_foods]
    total_heat_level = 0
    for num in heat_levels:
        total_heat_level += num
    return (total_heat_level/len(heat_levels))
#get_average_heat_level(spicy_foods)   

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return (spicy_foods) 

#create_spicy_food(spicy_foods, 90)
