list1 = [1, 2, 3, 5, 8, 15, 23, 38]

def select(f, col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

res = select(int, list1)
print(res)
res = where(lambda x: x % 2 == 0, res)

print(res)

res = select(lambda x: (x, x**2), res)

print(type(res))
print(res)