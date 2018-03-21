import time

def date(day,month,year):
    print(day , "/" , month , "/" , year )
    return

d = 0
m = 1
y = 2018


for i in range(1,400):
    d += 1
    # time.sleep(86400)
    # un comment the line that is apove this line if you want the day digit to change every 24 hours .

    if d == 31 and m == 12:
        y +=1
        m = 1


    if d ==31:
        m +=1

    if d == 31:
        d = 1


    date(d,m,y)

