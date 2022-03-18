answer = int (input("Введите продолжительность времени"))
s = answer%60
m = (answer//60)%60
h = (answer//60)//60%24
d = ((answer//60)//60)//24
while answer != 0:
    if answer < 60:
        print("seconds", answer)
        break
    elif h <= 0:
        print("minutes", m, "seconds", s)
        break
    elif d <= 0:
        print("hours", h, "minutes", m, "seconds", s)
        break
    elif d > 0:
        print ("days",d,"hours",h,"minutes",m, "seconds", s)
        break