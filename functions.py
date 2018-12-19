def squared(x):
    """Returns x squared.
    :param x: int.
    :return: int square of x."""
    return x**2


def printout(string):
    """Print out a string.
    :param string: string
    no return
    """
    print(string)


def madlibs(a, b, c, d='hyena', e='butt heads'):
    """Print out a very short 'Mad Libs' type string.
    :param a: a string noun
    :param b: a string noun.
    :param c: a string verb.
    :param d: a string noun.
    :param e: a string verb."""
    str1 = f'{a} went out to find {b}. It was {c}.'
    str1 += f' A {d} was around, trying to {e}.'
    return str1


print(squared(3))
print('Hiya')
print(madlibs("Dwayne Johnson", "a shoe", "dancing"))
