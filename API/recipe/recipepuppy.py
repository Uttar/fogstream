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
