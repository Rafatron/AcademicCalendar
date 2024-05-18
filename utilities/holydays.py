import datetime as dt
import tkinter as tk
#https://www.fagricipni.com/library/general/orthodox-easter.html

def Easter_Ortho(year):
    if year<0 or year>33807:
        raise ValueError("This function only valid between 0 and 33807")
    silver=year%19
    pfm=21+(19*silver+15)%30
    dow=(pfm+year+year//4)%7
    easter=pfm+7-dow
    easter=easter-2+year//100-year//400
    month=3+(5*easter-3)//153
    day=easter-(153*month-457)//5
    return (month,day)

def holidays(year, d=0):
    if d==0:
        year = int(year.get())
        d = dt.datetime(year, 1, 1)
    else:
        d = dt.datetime(year, 1, 1)

    list = [
        "24-12",
        "25-12",
        "26-12",
        "27-12",
        "28-12",
        "29-12",
        "30-12",
        "31-12",
        "1-1",
        "2-1",
        "3-1",
        "4-1",
        "5-1",
        "6-1",
        "7-1",
        "25-3",
        "1-5",
        "15-8",
        "28-10",
        "17-11",
        "30-11"
    ]

    d = dt.datetime(d.year, Easter_Ortho(d.year)[0], Easter_Ortho(d.year)[1]) #sunday of easter
    dd = d - dt.timedelta(days=6) #monday of easter
    for i in range(14):
        ddd = dd + dt.timedelta(days=i)
        list.append(f'{ddd.day}-{ddd.month}')

    dd = d + dt.timedelta(days=50) #hagiou pneumatos
    list.append(f'{dd.day}-{dd.month}')

    
    return list
    

if __name__ == '__main__':
    holidays()