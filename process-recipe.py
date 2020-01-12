import json
import urllib.request, json 
with urllib.request.urlopen("https://raw.githubusercontent.com/LeaVerou/forkgasm/master/recipes.json") as url:
    data = json.loads(url.read().decode())


# Recipe
recipe_counter = 1
ingredients_count = 1

json_result = []

for recipe in data['recipe']:
    steps_str = ""
    
    for step in recipe['step']:
        print(step)
        steps_str += (step['description'] + ", ")

    recipe_instance = {
        'model': "ar.Recipe",
        'pk': recipe_counter,
        'fields': {
            'name':recipe['name'],
            'source':recipe['image'],
            'instructions': steps_str,
        }
    }
    json_result.append(recipe_instance)
        

    for ingredient in recipe['ingredient']:
        quantity = None
        unit = None
        name = None
        if 'unit' in ingredient:
            unit = ingredient['unit']
        if 'quantity' in ingredient:
            quantity = ingredient['quantity'] 
        if 'name' in ingredient:
            name = ingredient['name'] 
        ingredient_instance = {
        'model': "ar.Ingredients",
        'pk': ingredients_count,
        'fields': {
            'name':name,
            'recipe':recipe_counter,
            'quantity':quantity,
            'unit': unit
            }
        }
        json_result.append(ingredient_instance)
        ingredients_count += 1
    
    recipe_counter += 1

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_result, f, ensure_ascii=False, indent=4)

# [
#   {
#     "model": "myapp.person",
#     "pk": 1,
#     "fields": {
#       "first_name": "John",
#       "last_name": "Lennon"
#     }
#   },
#   {
#     "model": "myapp.person",
#     "pk": 2,
#     "fields": {
#       "first_name": "Paul",
#       "last_name": "McCartney"
#     }
#   }
# ]