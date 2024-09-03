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
    return [meal["name"]for meal in spicy_foods ]
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return[meal for meal in spicy_foods if meal["heat_level"]>5]
print(get_spiciest_foods(spicy_foods))    


def print_spicy_foods(spicy_foods):
    for meal in spicy_foods:
        heat_level= "🌶" * meal["heat_level"]
        print(f"{meal['name']}({meal['cuisine']})| Heat Level:{heat_level}")
print(print_spicy_foods(spicy_foods))        
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for meal in spicy_foods:
        if meal["cuisine"]==cuisine:
            return meal
    return None        
 

def print_spiciest_foods(spicy_foods):
    for meal in spicy_foods:
         if meal["heat_level"] > 5:
            heat_level = "🌶" * meal["heat_level"]
            print(f"{meal['name']} ({meal['cuisine']}) | Heat Level: {heat_level}")
print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total_heat = sum(meal["heat_level"] for meal in spicy_foods)
    num_foods = len(spicy_foods)
    try:
        average_heat = total_heat / num_foods
        return average_heat
    except:
        if num_foods == 0:
            return 0

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
print(create_spicy_food(spicy_foods,  {
    "name": "Pilau",
    "cuisine": "kenyan",
    "heat_level": "2",
}))