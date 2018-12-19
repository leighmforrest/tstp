def half(x):
    """
    Divide an integer in two.
    :param x: int
    :return: int quotient of x and 2
    """
    return x // 2


def quadruple(x):
    """
    Multiply an x by 4.
    :param x: int
    :return: integer product of x and 4
    """
    return x * 4

if __name__ == '__main__':
    x = half(6)
    x = quadruple(x)
    print(f"The result is {x}.")
    
