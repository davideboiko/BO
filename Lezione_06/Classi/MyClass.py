class MyClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

persona1:MyClass = MyClass("bo", 22, "bobo")
persona2:MyClass = MyClass("bo1", 23, "bobo1")
persona3:MyClass = MyClass("bo2", 24, "bobo2")

print(f"Ciao {persona1.x} eta {persona1.y} figli {persona1.z}")
