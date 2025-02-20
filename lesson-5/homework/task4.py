import math
from statistics import mean as mn
from statistics import median as md

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = []
    tuitions = []

    for i in range(len(universities)):
        students.append(universities[i][1])
        tuitions.append(universities[i][2])
    
    return students, tuitions

def mean(data):
    
    mean_value = mn(data)
    return mean_value
    

def median_f(data):
    median_value = md(data)
    
    return median_value

students, tuitions = enrollment_stats(universities)

print("******************************")

print(f"Total students: {sum(students)}")
print(f"Total tuition: {sum(tuitions)}\n")

print(f"Student mean: {round(mn(students), 2)}")
print(f"Student median: {md(students)}\n")

print(f"Tuition mean: {round(mn(tuitions), 2)}")
print(f"Tuition median: {md(tuitions)}")

print("******************************")
