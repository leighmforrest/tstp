class Square:
    square_list = []
    def __init__(self, side):
        self.side = side
        self.square_list.append((side))

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side = new_size
        if self.side < 0:
            self.side = 0

    def __repr__(self):
        return f"{self.side} by {self.side} by {self.side} by {self.side}"

def is_same_square(square_1, square_2):
    return square_1 is square_2

if __name__ == '__main__':
    # Exercises 1 and 2
    square_1 = Square(3)
    print(square_1)
    print("Square Perimeter:", square_1.calculate_perimeter())
    # Add new squares but no references
    Square(29)
    Square(69)
    print(Square.square_list)

    # Exercise 3
    mutt = Square(3)
    jeff = mutt
    print("Mutt:", mutt)
    print("Jeff:", jeff)
    print("Mutt is Jeff:", is_same_square(mutt, jeff))

    jeff = Square(4)
    print("New Jeff:", jeff)
    print("Mutt is Jeff:", is_same_square(mutt, jeff))
