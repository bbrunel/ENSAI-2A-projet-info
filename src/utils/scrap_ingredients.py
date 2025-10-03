import json
import time
import urllib.request

data = []
i = 1
while i < 616:
    try:
        with urllib.request.urlopen(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid={i}") as url:
            res = json.loads(url.read().decode())
            if res is not None and res['ingredients'] is not None:
                for ingredient in res['ingredients']:
                    data.append(ingredient)
        i += 1
    except:
        print(i) # homemade pogress bar
        time.sleep(10)

print(len(data))
with open('ingredients.json', 'w') as f:
    f.write(json.dumps(data))