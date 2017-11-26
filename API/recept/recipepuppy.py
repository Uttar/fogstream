'''
http://www.recipepuppy.com/about/api
Ингредиенты берём из файла ing.txt, . Список возможных
Salt Butter Flour Water Eggs Milk Vanilla Extract Sugar Garlic Brown Sugar Olive Oil Vegetable Oil Black Pepper
Cinnamon Baking Powder Baking Soda Lemon Juice Parmesan Cheese Cheddar Cheese Garlic Powder Sour Cream Celery
Mayonnaise Nutmeg Cornstarch Honey Shortening Soy Sauce Worcestershire Sauce Paprika Chicken Broth Orange Juice
Raisins Chili Powder Onions Semisweet Chocolate Chips Cumin Margarine Beef Ginger'''

import urllib.request
import json

with open('ing.txt', 'r') as f:
    ing = f.read().replace(' ', ',').lower()
    f.close()

url = 'http://www.recipepuppy.com/api/?i=' + ing
req = urllib.request.Request(url)
response = urllib.request.urlopen(req).read()
js = json.loads(response.decode('utf-8'))

if not js['results']:
    print("Ничего не можем приготовить.")
    exit()

print('Итак, мы можем приготовить:')
for rec in js['results']:
    print(rec['title'].rstrip().lstrip() + ' - (' + rec['ingredients'] + ')' + ' - ' + rec['href'])
