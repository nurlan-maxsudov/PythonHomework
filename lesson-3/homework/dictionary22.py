my_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "tomato": "vegetable",
    "grape": "fruit",
    "cucumber": "vegetable"
}

new_dic = {key: value for key, value in my_dict.items() if value == "fruit"}

print(new_dic)