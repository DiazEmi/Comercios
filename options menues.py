# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:03:28 2021

@author: emili
"""

import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

options = tk.StringVar(my_w)
options.set("One") # default value

l1 = tk.Label(my_w,  text='Select One', width=10 )  
l1.grid(row=2,column=1) 

options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

om1 =tk.OptionMenu(my_w, options, *options_list)
om1.grid(row=2,column=2) 

b1 = tk.Button(my_w,  text='Show Value', command=lambda: my_show() )  
b1.grid(row=2,column=3) 

str_out=tk.StringVar(my_w)
str_out.set("Output")

l2 = tk.Label(my_w,  textvariable=str_out, width=10 )  
l2.grid(row=2,column=4) 

def my_show():
    str_out.set(options.get())

my_w.mainloop()