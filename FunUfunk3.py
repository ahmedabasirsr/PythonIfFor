def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

outer(3,7)