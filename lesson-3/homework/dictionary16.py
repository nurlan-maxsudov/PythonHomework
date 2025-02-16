person = {
    "name": "Alice",
    "age": 25,
    "address": {
        "city": "New York",
        "zip_code": "10001"
    }
}

is_nested = False

for value in person.values():
    if type(value) == dict:
        is_nested = True

if is_nested:
    print("A nested dictionary")
else:
    print("Not a nested dictionary")