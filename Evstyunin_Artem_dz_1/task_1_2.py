my_list = list(i**3 for i in range(1,1001,2))
sum = 0 # общая сумма
sum_2 = 0 # общая сумма b
for num in my_list:
    sum_num = 0 # сумма цифр в числе
    num_1 = num
    while True:
        sum_num += num_1 % 10
        num_1 //= 10
        if num_1 < 10:
            sum_num += num_1 % 10
            break
    if sum_num % 7 == 0:
        sum += num
for num in my_list:
    sum_num_2 = 0 # сумма цифр для b
    num_2 = num + 17 # число + 17
    while True:
        sum_num_2 += num_2 % 10
        num_2 //= 10
        if num_2 < 10:
            sum_num_2 += num_2 % 10
            break
    if sum_num_2 % 7 == 0:
        sum_2 += num + 17
print ("a",sum,"b",sum_2)





