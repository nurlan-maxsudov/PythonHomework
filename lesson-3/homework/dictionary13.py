countries_and_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}

inverted_dic = {}

for key, value in countries_and_capitals.items():
    inverted_dic[value] = key

print(inverted_dic)