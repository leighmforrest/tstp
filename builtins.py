def float_string(str1):
    """
    Return a string converted to a float.
    param: str1 a string
    :return: str1 converted to a float or 0.0
    """
    try:
        return float(str1)
    except:
        return 0.0


if __name__ == '__main__':
    print(float_string('12.5'))
    print(float_string('bleen'))
