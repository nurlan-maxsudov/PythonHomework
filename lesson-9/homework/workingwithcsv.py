import csv

data = [["Alex",20,"Developer"],
        ["Jorj",30,"Writer"],
        ["Bob",24,"Reader"]]
filename = ["Name", "Age", "Occupation"]

with open("output.csv", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(filename)
    writer.writerows(data)

