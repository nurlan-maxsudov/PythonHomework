my_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "tomato": "vegetable",
    "grape": "fruit",
    "cucumber": "vegetable"
}

unique_values = []

for value in my_dict.values():
    if value not in unique_values:
        unique_values.append(value)

print(len(unique_values))