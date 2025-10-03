import json
import urllib.request

data = []
i = ord('a')
while i <= ord('z'):
    with urllib.request.urlopen(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={chr(i)}") as url:
        res = json.loads(url.read().decode())['drinks']
        if res is not None:
            for cocktail in res:
                data.append(cocktail)
    i += 1

print(len(data))
with open('cocktails.json', 'w') as f:
    f.write(json.dumps(data))
