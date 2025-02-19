my_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "tomato": "vegetable",
    "grape": "fruit",
    "cucumber": "vegetable"
}

value_to_count = "fruit"

count = list(my_dict.values()).count(value_to_count)

print(count)