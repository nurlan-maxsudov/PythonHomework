my_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "tomato": "vegetable",
    "grape": "fruit",
    "cucumber": "vegetable"
}

keys = []

val = "fruit"

for key, value in my_dict.items():
    if value == val:
        keys.append(key)

print(keys)