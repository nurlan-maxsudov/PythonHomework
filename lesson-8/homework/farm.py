class Animal:
    total_animals = 0
    
    def __init__(self, name, weight, energy, age, is_hungry=False):
        if not self.is_valid_str(name):
            raise ValueError("Name must be a string")
        self.name = name
        if not self.is_valid_int(weight):
            raise ValueError("Weight must be an integer")
        self.weight = weight
        if not self.is_valid_int(energy):
            raise ValueError("Energy must be an integer") 
        self.energy = energy
        if not self.is_valid_int(age):
            raise ValueError("Age must be an integer")
        self.age = age
        self.is_hungry = is_hungry
        Animal.total_animals += 1  

    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}, weighs {self.weight} kg, {self.age} years old"
    
    def display_info(self):
        print(self.__str__())

    def eat(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f'{self.name} has eaten')
        else:
            print(f'{self.name} is full')
    
    def make_sound(self):
        return self.sound  

    def sleep(self):
        if self.energy < 20:
            print(f"{self.name} is sleeping")
        else:
            print(f"{self.name} is awake")

    @staticmethod
    def is_valid_int(arg):
        return isinstance(arg, int) and arg > 0
    
    @staticmethod
    def is_valid_str(arg):
        return isinstance(arg, str) and arg != ""

    @staticmethod
    def is_valid_float(arg):
        return isinstance(arg, float) and arg > 0

    @classmethod
    def num_of_animals(cls):
        return cls.total_animals

class Cow(Animal):
    def __init__(self, name, weight, energy, age, milk_production, breed, sound="Moo", is_hungry=False):
        super().__init__(name, weight, energy, age, is_hungry)
        if not self.is_valid_float(milk_production):
            raise ValueError("The amount of milk must be a number")
        self.milk_production = milk_production
        if not self.is_valid_str(breed):
            raise ValueError("The breed of the cow must be a string")
        self.breed = breed
        self.sound = sound
    
    def is_mature_for_milk(self):
        return 2 < self.age < 13
    
    def give_milk(self):
        if self.energy > 60 and not self.is_hungry and self.is_mature_for_milk():
            print(f"{self.name} is ready to give {self.milk_production} litres of milk")

class Sheep(Animal):
    def __init__(self, name, weight, energy, age, wool_length, breed, sound="Baa", is_hungry=False):
        super().__init__(name, weight, energy, age, is_hungry)
        if not self.is_valid_float(wool_length):
            raise ValueError("Length of the wool must be a number")
        self.wool_length = wool_length
        if not self.is_valid_str(breed):
            raise ValueError("Breed must be a string")
        self.breed = breed
        self.sound = sound
    
    def shear_wool(self):
        if self.wool_length > 20:
            self.wool_length = 5
            print(f"Wool of {self.name} is sheared")
        else:
            print(f"{self.name} does not have enough wool to shear yet.")

class Chicken(Animal):
    def __init__(self, name, weight, energy, age, egg_production, breed, sound="Cluck", is_hungry=False):
        super().__init__(name, weight, energy, age, is_hungry)
        if not self.is_valid_int(egg_production):
            raise ValueError("Number of eggs must be an integer")
        self.egg_production = egg_production
        if not self.is_valid_str(breed):
            raise ValueError("Breed must be a string")
        self.breed = breed
        self.sound = sound
    
    def is_mature_for_eggs(self):
        return 1 < self.age < 8
    
    def lay_eggs(self):
        if self.energy > 60 and not self.is_hungry and self.is_mature_for_eggs():
            print(f"{self.name} is ready to give {self.egg_production} eggs")


