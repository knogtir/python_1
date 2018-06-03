def my_abs (x):
    if not isinstance (x, (int, float)):
        raise TypeError("类型不正确")
    if x >= 0:
        return x
    elif x < 0:
        return (-x)
