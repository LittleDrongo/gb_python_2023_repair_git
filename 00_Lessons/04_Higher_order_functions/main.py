# def f(x):
#     return x*x

# print(
#     f(5)
# )


# calk1 = lambda a, b: a + b

# print(calk1( 5, 45))

""" ТЗ
    1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
    (число; квадрат числа).
    Пример: 1 2 3 5 8 15 23 38
    Получить: [(2, 4), (8, 64), (38, 1444)]
"""

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_res = []

print(list1)

for i in range(len(list1)):
    if list1[i] % 2 == 0:
            list_res.append(
                  (list1[i], list1[i]*list1[i])
            )
print(list_res)
        
#    Кортеж	        -	            +	                -	            (,)	            tuple()

print(list_res)