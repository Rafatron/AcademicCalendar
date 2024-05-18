import tkinter as tk
from tkinter import messagebox
from os import remove
import datetime as dt
import holydays as hd

sem1 = [8,9,10,11,12,1]
sem2 = [2,3,4,5,6]

def saving(place: tk , entry: tk ,combobox: tk ):
      data = place.get("1.0",'end-1c')
      data = f'{data}\n\n'
      date = entry.get()
      saving_period = combobox.get()
      day, month, year = date.split('/')
      dayz = int(day)
      monthz = int(month)
      year = int(year)

      if not data.lstrip() : 
           try:
                remove(f"{dayz:0>2}-{monthz:0>2}-{year}.cal")
                return
           except: return
           
      try:
           d = dt.datetime(year,monthz,dayz)
      except: 
           messagebox.showerror('Σφάλμα Ημερομηνίας', 'Σφάλμα: Μι-Έγκυρη Ημερομηνία')
           return

      def weekly(z):
           week_dates = []
           o = 0
           for i in range(0,53,1):
                dd = d+dt.timedelta(days=o)
                if dd.year == year + 1 and dd.month == 2:
                     break
                else: week_dates.append(dd)
                o += z
           for i in range(0, len(week_dates)):
                if f'{week_dates[i].day}-{week_dates[i].month}' not in hd.holidays(year, 1):
                    notes = open("{:0>2}-{:0>2}-{:0>4}.cal".format(week_dates[i].day,week_dates[i].month,week_dates[i].year), "w" , encoding = 'utf-8')
                    notes.write(data)
                    notes.close()
                else: pass

      def semester(z):
           week_dates = []
           o = 0
           for i in range(0,53,1):
               dd = d+dt.timedelta(days=o)
               if d.month in sem1:
                    if dd.month == 2:
                         break
                    else: week_dates.append(dd)
               elif d.month in sem2:
                    if dd.month == 7:
                         break
                    else: week_dates.append(dd)
               o += z
           for i in range(0, len(week_dates)):
                if f'{week_dates[i].day}-{week_dates[i].month}' not in hd.holidays(year, 1):
                    notes = open("{:0>2}-{:0>2}-{:0>4}.cal".format(week_dates[i].day,week_dates[i].month,week_dates[i].year), "w" , encoding = 'utf-8')
                    notes.write(data)
                    notes.close()
                else: pass


      if saving_period ==  'Σήμερα':
           notes = open(f"{day}-{month}-{year}.cal", "w" , encoding = 'utf-8')
           notes.write(data)
           notes.close()

      elif saving_period ==  'Εβδομαδιαία':
           weekly(7)

      elif saving_period ==  'Ανά δυο Εβδομάδες':
           weekly(14)
      
      elif saving_period ==  'Εβδομαδιαία για Εξάμηνο':
           semester(7)
      
      elif saving_period ==  'Ανά δυο Εβδομάδες για Εξάμηνο':
           semester(14)