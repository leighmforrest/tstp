import math


class Apple:
    def __init__(self, color, weight, worm=False):
        self.color = color
        self.weight = weight
        self.mold = 0
        self.worm = worm

    def rot(self, days, temp):
        self.mold = days * temp
    
    def __str__(self):
        string = f"The {self.color} apple weighs {self.weight} grams.\n"
        if self.mold > 0:
            string += f"Mold: {self.mold}\n"
        else:
            string += "There is no mold.\n"
        if self.worm:
            string += "There is a worm."
        else:
            string += "There is no worm."
        return string


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return f"<Triangle: {self.base}, {self.height}>"


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8):
        self.sides = []
        self.sides.append(s1)
        self.sides.append(s2)
        self.sides.append(s3)
        self.sides.append(s4)
        self.sides.append(s5)
        self.sides.append(s6)
        self.sides.append(s7)
        self.sides.append(s8)

    def calculate_perimeter(self):
        return sum(self.sides)

    def __str__(self):
        string = "<Hexagon:"
        # the data must be strings for joining output
        tmp = [str(i) for i in self.sides]
        
        string += ','.join(tmp)
        return string + '>'


if __name__ == '__main__':
    # Exercise 1
    apple_1 = Apple('Red', 100)
    apple_2 = Apple("Green", 120, True)
    apple_2.rot(2, 70)
    print(apple_1)
    print(apple_2)

    # Exercise 2
    circle_1 = Circle(1)
    circle_2 = Circle(12)
    print(circle_1.area())
    print(circle_2.area())

    # Exercise 3
    triangle_1 = Triangle(6, 3)
    print(triangle_1)
    print("Area:", triangle_1.area())

    # Exercise 4
    hex_1 = Hexagon(1,1,1,1,1,1,1,1)
    print(hex_1)
    print("The perimeter of hexagon 1 is", hex_1.calculate_perimeter())
