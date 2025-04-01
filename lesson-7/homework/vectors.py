class Vector:
    
    def __init__(self, *args):
        self.array = tuple(args)
        
    def __add__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*[a + b for a, b in zip(self.array, other.array)])
    
    def __sub__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Vecotrs must have the same dimensions for substraction.")
        return Vector(*[a - b for a, b in zip(self.array. other.array)])
    
    def __mul__(self, other):
         if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
         elif isinstance(other, Vector):  # Dot product
            if len(self.array) != len(other.array):
                raise ValueError("Vectors must have the same dimensions for multiplication.")
            return sum([a*b for a, b in zip(self.array, other.array)])
    
    def __div__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Vectors must have the same dimensions for multiplication.")
        return Vector(*[a/b for a, b in zip(self.array, other.array)])
    
    def magnitude(self):
        return (sum([x**2 for x in self.array]))**(1/2)
    
    def normalize(self):
        mag = (sum([x**2 for x in self.array]))**(1/2)
        
        return Vector(*[x/mag for x in self.array])
    
    def __str__(self):
        return f"{self.array}"

    
    
    
v1 = Vector(1, 2, 3)
v2 = Vector(2, 2, 2)
dot_product = v1 * v2
print(dot_product)
