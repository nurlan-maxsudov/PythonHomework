countries_and_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan" : "Tokyo",
    "Australia": "Canberra"
}

key = "Japan"

removed_key = countries_and_capitals.pop("Japan", "Key was not found")

print(removed_key)