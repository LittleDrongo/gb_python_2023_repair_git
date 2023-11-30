coins = [0, 1, 0, 1, 1, 1, 0]
# coins = [0, 1, 0, 1, 1, 0]

count_zero = 0
count_one = 0

for i in range(len(coins)):
        if coins[i] == 0:
                count_zero += 1
                print('add zero')
        if coins[i] == 1:
                count_one += 1
                print('add_one')

# if count_zero < count_one:
#         print(count_zero)
# else:
#         print(count_one)