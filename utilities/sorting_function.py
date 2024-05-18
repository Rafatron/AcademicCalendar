import tkinter as tk

def sorting_function(text:tk):
    data = text.get("1.0", 'end-1c')
    unsorted_string = data.split("\n")
    things_i_wanna_sort = []
    for i in unsorted_string:
        if ":" in i:
            things_i_wanna_sort.append((i, int(f'{i[0]}{i[1]}{i[3]}{i[4]}')))    
    things_i_wanna_sort.sort(key=lambda x: x[1])          
    things_i_wanna_return = []
    for i in things_i_wanna_sort:
        things_i_wanna_return.append(i[0])
    for i in unsorted_string:
        if i not in things_i_wanna_return:
            things_i_wanna_return.append(i)
    s = ""
    for i in things_i_wanna_return:
        s += str(i) + "\n\n"
    text.delete("1.0", "end")
    text.insert("1.0",s)