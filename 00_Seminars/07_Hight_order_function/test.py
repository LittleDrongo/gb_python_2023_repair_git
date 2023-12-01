def func():
    a = 2 + 2
    return a

def func(b, c):
    a = b + c
    return a

b, c = 2, 3

print(
    func(c, b)
)

# print(
#     func(c = 2, b = 2)
# )

func2 = lambda b, c : b + c
print(func2(5 , 5))

print(func2(b = 5 , c = 5))


def func3(*args, **kwargs):
    print(args)
    a = args[0] + args[1]
    return a

print(func3(5, 5, 5))