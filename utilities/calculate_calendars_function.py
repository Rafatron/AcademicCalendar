import tkinter as tk
import datetime

#days = {0: 'Δευτέρα', 1: 'Τρίτη', 2: 'Τετάρτη', 3: 'Πέμπτη', 4: 'Παρασκευή', 5: 'Σάββατο', 6: 'Κυριακή'}

def calculate_monthly_calendar(month, year):
    l = []
    for i in range(1, 32):
        date_exists = True
        try:
            datetime.datetime(int(year), int(month), int(i))
        except ValueError:
            date_exists = False

        if(date_exists):
            date_info = (int(i), int(month), int(year), int(datetime.datetime.strptime(f"{i}-{month}-{year}", "%d-%m-%Y").weekday()))
            l.append(date_info)
    return l