import requests
import json

var=requests.get("https://fr-en.openfoodfacts.org/category/pizzas/1.json")
var=json.loads(var.text)
for product in var["products"]:
    print (json.dumps(product,indent=2))