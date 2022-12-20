def IsLeapYear(y):
    x = True
    if y%100!=0 and y%4==0:
        return x
    if y%100==0 and y%400==0:
        return x
    else:
        return False
def MonthDays(m,y):
    if m==2:
        return 28 + IsLeapYear(y)
    else:
        if m==4 or m==6 or m==9 or m==11:
            return 30
        elif m==2:
            return 28
        else:
            return 31
def NextDate(d,m,y,k):
    d+=k
    while d>MonthDays(m,y):
        d-=MonthDays(m,y)
        m+=1
        if m>12:
            m=1
            y+=1
    return d,m,y
d,m,y = map(int,input().split())
k=int(input('k ='))
print(NextDate(d,m,y,k))