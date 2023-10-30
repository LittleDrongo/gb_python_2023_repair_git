# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# Пример:
# n = 385916 -> yes
# n = 123456 -> no

n = 385916

sum_left_side = 0
sum_right_side = 0

digit_count = 0
num = n
while num > 0:
    num = int(num / 10)
    digit_count += 1

center = int(digit_count / 2)

if digit_count % 2 == 0:
        while n > 0:
            i = digit_count
            while i > center:
                last_digit = n % 10
                n = int(n / 10)
                sum_right_side = sum_right_side + last_digit
                i -= 1
            while i > 0:
                last_digit = n % 10
                n = int(n / 10)
                sum_left_side = sum_left_side + last_digit
                i -= 1

if sum_left_side == sum_right_side:
     result = True
else:
     result = False

print(result)