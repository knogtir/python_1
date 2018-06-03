def outer(x):
    print(x)
    def inter(y):
        nonlocal x
        x *= x
        y = x-3
        return x, y
    return inter()


outer(3)(2)
