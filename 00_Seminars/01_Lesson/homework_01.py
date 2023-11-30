# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

number = 123
result = 0

while number > 0:
    part = int(number % 10)
    result = result + part
    number = int((number / 10))
print (result)