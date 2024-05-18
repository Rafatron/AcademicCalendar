import tkinter as tk
from tkinter import messagebox

def acces(year_entry: tk.Entry, day_date, month_number: str, date_entry: tk.Entry, text_field: tk.Text):
    year = year_entry.get() #year
    date_entry.delete(0, "end")
    if len(str(day_date)) == 1:
        day_date = f'0{day_date}'
    if month_number == "01" or month_number == "02" or month_number == "03" or month_number == "04" or month_number == "05" or month_number == "06":
        try:
            year = int(year) + 1
        except: 
            tk.messagebox.showerror("Μη έγκυρο έτος", "φρόντισε να είναι αριθμός!")
            return
        date_entry.insert(0, f'{day_date}/{month_number}/{year}')
    else:
        date_entry.insert(0, f'{day_date}/{month_number}/{year}')
    text_field.delete("1.0", "end")

    try:
        file = open(f'{day_date}-{month_number}-{year}.cal', "r", encoding="utf-8")
        noted_info = ""
        for lines in file:
            noted_info += lines
        text_field.insert("1.0", noted_info)
    except: pass   