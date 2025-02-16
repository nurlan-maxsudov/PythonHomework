from collections import defaultdict

default_dict = defaultdict(lambda: "Not Found")

default_dict["name"] = "Alice"
default_dict["age"] = 25

print(default_dict["name"]) 
 
print(default_dict["city"])  
