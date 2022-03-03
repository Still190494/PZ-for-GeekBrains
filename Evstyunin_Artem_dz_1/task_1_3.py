num = 0
while num != 100:
    num = num + 1
    a = num // 10
    b = num % 10
    if b == 1 and a + b != 2:
        print (num, ("Процент"))
    if b!= 1 and b < 5 and b != 0 and a != 1:
        print(num, ("Процента"))
    else:
        if b !=1 or a + b == 2:
            print(num, ("Процентов"))