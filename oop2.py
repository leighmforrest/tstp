class Shape:
    def what_am_i(self):
        return "I am a shape!"


class Rectangle(Shape):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def calculate_perimeter(self):
        return (2 * self.s1) + (2 * self.s2)

    def __str__(self):
        return f"<Rectangle: 2 sides of {self.s1} and 2 sides of {self.s2}>"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side = new_size
        if self.side < 0:
            self.side = 0

    def __str__(self):
        return f"<Square: {self.side} each side>"



if __name__ == '__main__':
    # Exercise 1
    rectangle_1 = Rectangle(2,4)
    square_1 = Square(3)
    print(rectangle_1)
    print(square_1)
    print("Rectangle Perimeter:", rectangle_1.calculate_perimeter())
    print("Square Perimeter:", square_1.calculate_perimeter())

    # Exercise 2
    size = -4
    print("Square changes size to", size)
    square_1.change_size(size)
    print(square_1)
    print("Square's new perimeter:", square_1.calculate_perimeter())

    # Exercise 3
    print("Rectangle says:", rectangle_1.what_am_i())
    print("Square says:", square_1.what_am_i())
    
