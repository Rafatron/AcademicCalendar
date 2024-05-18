import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os
import sys

parent_dir = os.path.dirname(os.path.realpath(__file__))  # using functions
sys.path.append(f'{parent_dir}/utilities')
img_path = os.path.join(f'{parent_dir}/utilities/emblem.gif') # emblem
ico_path = os.path.join(f'{parent_dir}/utilities/calendar.ico') # icon
os.chdir(f'{parent_dir}/data') #running program on /data to save properly

import save_function as sf
import calculate_calendars_function as ccf
import open_function as of
import holydays as hd
import sorting_function as so



class GUI():
    days_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_nameGR = ["Δευτέρα", "Τρίτη","Τετάρτη", "Πέμπτη", "Παρασκευή", "Σαββάτο", "Κυριακή"]

    semester_1 = ["August", "September", "October", "November", "December", "January"]
    semester_2 = ["February", "March", "April", "May", "June"]

    months_in_numbers = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    numbers_in_months = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 6:'July', 8: 'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    days_in_numbers = {0: "sunday", 1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}
    meng_2_mgr = {'January':'Ιανουάριος', 'February':'Φεβρουάριος', 'March':'Μάρτιος', 'April':'Απρίλιος', 'May':'Μάιος', 'June':'Ιούνιος', 'July':'Ιούλιος', 'August':'Αύγουστος', 'September':'Σεπτέμβριος', 'October':'Οκτώβριος', 'November':'Νοέμβριος', 'December':'Δεκέμβριος'}
    mgr_2_meng = {'Ιανουάριος':'January', 'Φεβρουάριος':'February', 'Μάρτιος':'March', 'Απρίλιος':'April', 'Μάιος':'May', 'Ιούνιος':'June', 'Ιούλιος':'July', 'Αύγουστος':'August', 'Σεπτέμβριος':'September', 'Οκτώβριος':'October', 'Νοέμβριος':'November', 'Δεκέμβριος':'December'}

    c = True

    current_selected_month = months_in_numbers[datetime.today().strftime("%B")]

    #Today's day
    year, month, day = str(datetime.today().strftime('%Y-%m-%d')).split("-")

    list_of_monthly_dates = []
    
    
    def __init__(self, root):      
        root.resizable(False, False)
        root.title("Ακαδημαϊκό Ημερολόγιο")
        root.iconbitmap(ico_path)
        self.c = True
        
        #my frames
        self.main_left = ttk.Frame(root, width = 300)
        self.left = ttk.Frame(self.main_left, width = 300)
        self.left1 = ttk.Frame(self.main_left, width = 300)
        self.right = ttk.Frame(root, width = 300)
        self.mid = ttk.Frame(root, width = 300)

        #flair button
        self.flair = tk.Button(self.left1, width=20, text="Λειτουργικότητα\n(πάτα με)", height=4, command = self.flair).grid(row=0, column=0)

        #my month and year
        self.lab3 = tk.Label(self.mid, text = GUI.meng_2_mgr[datetime.today().strftime("%B")])
        self.yeare = tk.Entry(self.mid, width=15)
        
        if int(GUI.month) == 1 or int(GUI.month) == 2 or int(GUI.month) == 3 or int(GUI.month) == 4 or int(GUI.month) == 5 or int(GUI.month) == 6 :
            self.yeare.insert(0, int(datetime.today().strftime("%Y"))-1)
        else:
            self.yeare.insert(0, datetime.today().strftime("%Y"))
        

        #academic year
        self.yeare.bind('<KeyRelease>', self.updateAdvance)
        self.advance = tk.Label(self.mid, text =f'-{int(self.yeare.get())+1}')

        #text appearing button
        self.text_but = tk.Button(self.right, text="Οργάνωσε σημείωση", command = lambda: self.to_sort())

        # date entry as save button
        self.date_entry = tk.Entry(self.right)
        self.notes_date_text = f"{GUI.day}/{GUI.month}/{GUI.year}"
        self.date_entry.insert(0, self.notes_date_text)

        self.current_var = tk.StringVar()
        self.saving_period_combobox = ttk.Combobox(self.right, textvariable=self.current_var, text="Σήμερα", foreground="gray", width=27)

        #This day: μονο για αυτην την μερα, Weekly: καθε βδομαδα του εξαμήνου εκτος από αργιες κλπ, Monthly: καθε μήνα του εξαμήνου εκτος από αργίες, Semester: καθε εξάμηνο
        self.saving_period_combobox['values'] = ('Σήμερα', 'Εβδομαδιαία', 'Ανά δυο Εβδομάδες', 'Εβδομαδιαία για Εξάμηνο', 'Ανά δυο Εβδομάδες για Εξάμηνο')
        self.saving_period_combobox['state'] = 'readonly'
        
        self.add = tk.Button(self.right, text="Αποθήκευσε σημείωση", command = lambda: self.saver(GUI.mgr_2_meng[self.lab3.cget('text')]))

        #my text
        self.texte = tk.Text(self.right, height=53, width=20)
        try:
            todays_note = open(f'{GUI.day}-{GUI.month}-{GUI.year}.cal', 'r', encoding="utf-8")
            noted_info = ""
            for lines in todays_note:
                noted_info += lines
            self.texte.insert("1.0", noted_info)
        except: pass

        #my days
        self.day_button = []
        for i in range(1, 32):
            self.day_button.append(tk.Button(self.mid, text=str(i), width=20, height=8, bg="white", command= lambda i=i: of.acces( self.yeare, str(i), GUI.current_selected_month, self.date_entry, self.texte )))
        self.day_label = []
        for i in GUI.days_nameGR:
            self.day_label.append(tk.Label(self.mid, text = i, width = 20, height = 4))
        for i in range(len(self.day_label)):
            self.day_label[i].grid(row=1, column=i)

        #my months
        self.change_semester_button = tk.Button(self.left, text = "Αλλαγή Εξαμήνου", width = 25, height=3, font = 20, command = lambda:self.change_semester())
        self.select_month_button = []
        for i in GUI.semester_1:
            self.select_month_button.append(tk.Button(self.left, text = GUI.meng_2_mgr[i], width = 25, height=3, font = 20, command = lambda i=i: self.change_calendar(i)))

        #emblem
        self.image = tk.PhotoImage(file=img_path)
        self.emblem = tk.Label(self.left1, image = self.image, width=250, height=250)
        
        #packing frames
        self.main_left.pack(expand = True, fill = "both", side = 'left')
        self.left.pack(expand=True, fill = "both", side='top', anchor = "n")
        self.left1.pack(expand=True, side='bottom', anchor = "s")
        self.right.pack(expand=True, fill='both', side='right')
        self.mid.pack(expand=True, fill='both', anchor='center')

        #packing left
        self.change_semester_button.grid(row = 0, column = 0, sticky = "nesw")
        for i in range(1, 7):
            self.select_month_button[i-1].grid(row = i, column = 0, sticky = "nesw")

        #packing left1
        self.emblem.grid(row=9, column=0, sticky = "nesw")

        #packing right
        self.text_but.grid(row=0, column=0, padx=1, sticky = "nesw")
        self.date_entry.grid(row=0, column=1, padx=1,sticky = "nesw")
        self.saving_period_combobox.set('Σήμερα')
        self.saving_period_combobox.grid(row = 0, column = 2, sticky = "nesw")
        self.add.grid(row=0, column=3, sticky = "nesw")
        self.texte.grid(row=1, column=0, columnspan=4, sticky ="nsew")

        #packing middle
        self.lab3.grid(row=0, column=2, columnspan=3)
        self.yeare.grid(row=0,column=5, sticky="e")
        self.advance.grid(row=0, column=6,sticky="w")

        for i in self.semester_1:
            if self.months_in_numbers[i] == self.month:
                self.change_calendar(i)
        for i in self.semester_2:
            if self.months_in_numbers[i] == self.month:
                self.change_calendar(i)

        if self.month == "02" or self.month == "03" or self.month == "04" or self.month == "05" or self.month == "06":
            self.change_semester()

    def change_semester(self):
        if GUI.c:
            self.select_month_button[len(self.select_month_button) - 1].destroy()
            self.select_month_button = []
            for i in GUI.semester_2:
                self.select_month_button.append(tk.Button(self.left, text = GUI.meng_2_mgr[i], width = 20, height=3, font = 20, command = lambda i=i:self.change_calendar(i)))
            for i in range(1,6):
                self.select_month_button[i-1].grid(row = i, column = 0, sticky = "nesw") 
            GUI.c = False
        else:
            self.select_month_button = []
            for i in GUI.semester_1:
                self.select_month_button.append(tk.Button(self.left, text = GUI.meng_2_mgr[i], width = 20, height=3, font = 20, command = lambda i=i:self.change_calendar(i)))
            for i in range(1,7):
                self.select_month_button[i-1].grid(row = i, column = 0, sticky = "nesw")
            GUI.c = True

    def change_calendar(self, month):
        GUI.current_selected_month = GUI.months_in_numbers[month]
        self.lab3.grid_forget()
        self.lab3 = tk.Label(self.mid, text = GUI.meng_2_mgr[month])
        self.lab3.grid(row=0, column=2, columnspan=3)
        o=1
        for z in self.day_button:
            z.config(bg="white")
            z.config(text=o)
            o+=1
            
        for i in self.day_button:
            i.grid_forget()

        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June':
            GUI.list_of_monthly_dates = ccf.calculate_monthly_calendar(GUI.months_in_numbers[month], str(int(self.yeare.get())+1))
            x, column_count = 2, GUI.list_of_monthly_dates[0][3]
            for i in range(0, len(GUI.list_of_monthly_dates)):
                t = GUI.list_of_monthly_dates[i]
                self.day_button[i].grid(row=x,column=t[3], sticky = 'nesw')
                if t[3]== 5 or t[3] == 6:
                    self.day_button[i].config(bg="gray")
                if f'{i+1}-{t[1]}' in hd.holidays(int(self.yeare.get()) +1, 1):
                    self.day_button[i].config(bg="light blue")
                if os.path.exists(f'{i+1:0>2}-{t[1]:0>2}-{int(self.yeare.get())+1}.cal'):
                    self.day_button[i].config(bg="#7FFF00", text=f"*{i+1}*")
                    file = open(f'{i+1:0>2}-{t[1]:0>2}-{int(self.yeare.get())+1}.cal', "r", encoding="utf-8")
                    noted_info = ""
                    for lines in file:
                        noted_info += lines
                    if "##test" in noted_info and "##study" in noted_info:
                        self.day_button[i].config(text=f"[(*{i+1}*)]", bg="orange")
                    elif "##test" in noted_info:
                        self.day_button[i].config(text=f"(*{i+1}*)", bg="#FF6347")
                    elif "##study" in noted_info:
                        self.day_button[i].config(text=f"[*{i+1}*]", bg="#DDA0DD")

                column_count += 1
                if column_count >= 7:
                    column_count = 0
                    x += 1
        else:
            GUI.list_of_monthly_dates = ccf.calculate_monthly_calendar(GUI.months_in_numbers[month], str(self.yeare.get()))
            x, column_count = 2, GUI.list_of_monthly_dates[0][3]
            for i in range(0, len(GUI.list_of_monthly_dates)):
                t = GUI.list_of_monthly_dates[i]
                self.day_button[i].grid(row=x,column=t[3], sticky = 'nesw')
                if t[3]== 5 or t[3] == 6:
                    self.day_button[i].config(bg="gray")
                if f'{i+1}-{t[1]}' in hd.holidays(self.yeare):
                    self.day_button[i].config(bg="light blue")
                if os.path.exists(f'{i+1:0>2}-{t[1]:0>2}-{self.yeare.get()}.cal'):
                    self.day_button[i].config(bg="#7FFF00", text=f"*{i+1}*")
                    file = open(f'{i+1:0>2}-{t[1]:0>2}-{self.yeare.get()}.cal', "r", encoding="utf-8")
                    noted_info = ""
                    for lines in file:
                        noted_info += lines
                    if "##test" in noted_info and "##study" in noted_info:
                        self.day_button[i].config(text=f"[(*{i+1}*)]", bg="orange")
                    elif "##test" in noted_info:
                        self.day_button[i].config(text=f"(*{i+1}*)", bg="#FF6347")
                    elif "##study" in noted_info:
                        self.day_button[i].config(text=f"[*{i+1}*]", bg="#DDA0DD")

                column_count += 1
                if column_count >= 7:
                    column_count = 0
                    x += 1
    
    def updateAdvance(self, event):
        try:
            self.advance.config(text=f'-{int(self.yeare.get())+1}')
            if int(self.yeare.get()) > 3999:
                tk.messagebox.showerror("Μη έγκυρο έτος", "ΠΡΟΣΟΧΗ!\nΤο ημερολόγιο έχει ακρίβεια μέχρι το έτος 3999\nτο πρόγραμμα θα συνεχιστεί κανονικά, χρησιμοποιείται με δική σας επιμέλεια\n\nμέχρι τοτε επιτυγχάνεται ο ακριβής υπολογισμός του πάσχα")
        except: self.advance.config(text=f'error')
    
    def flair(self):
        tk.messagebox.showinfo("Λειτουργικότητα", "<[Flairs]>:\nπράσινο: η σημείωση αποθηκεύτηκε, συμβολίζεται επίσης με **\n\nκόκκινο: εξέταση, συμβολίζεται επίσης με (**) και ορίζεται πληκτρολογώντας ##test οπουδήποτε στη σημείωση\n\nμωβ: μελέτη, συμβολίζεται επίσης με [**] και ορίζεται πληκτρολογώντας ##study οπουδήποτε στη σημείωση\n\nπορτοκαλί: μελέτη και εξέταση, που συμβολίζονται με [(**)], μπορούν να οριστούν πληκτρολογώντας και τα δύο flair\n\n\n<[Οργάνωση]>:\nπληκτρολογήστε την ώρα μπροστά από κάθε γραμμή, μορφοποιημένη ως εξής (xx:xx) και θα ταξινομηθούν με χρονολογική σειρά πατώντας το κουμπί [Οργάνωσε σημείωση]")

    def to_sort(self):
        so.sorting_function(self.texte)     

    def saver(self, month):
        sf.saving(self.texte, self.date_entry, self.saving_period_combobox)
        self.change_calendar(month)


if __name__ == "__main__":          
    root = tk.Tk()
    GUI(root)
    root.mainloop()