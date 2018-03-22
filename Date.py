import time

def date(day,month,year):
    print(day , "/" , month , "/" , year )
    return

d = 0
m = 1
y = 2000


while True :



    d += 1
    #time.sleep(86400)  
    # un comment the line that is above this line if you want the day digit to change every 24 hours .

    # if y % 4 == 0 and m == 2 and d == 29 :
    #     d = 1
    #     m += 1

    if d == 32 and m == 12:
        y +=1
        m = 0



    if d == 32:
        m += 1

    if d == 32:
        d = 1

    if m == 2 and d == 29 and y % 4 != 0 :
        d = 1
        m+= 1
    elif m == 2 and d == 30 and y % 4 == 0:
        d = 1
        m+= 1



    if m == 4 and d == 31 :
        d = 1
        m += 1

    if m == 6 and d == 31 :
        d = 1
        m += 1

    if m == 9 and d == 31 :
        d = 1
        m += 1

    if m == 11 and d == 31 :
        d = 1
        m += 1





    date(d,m,y)

