# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:36:25 2021

@author: emili
"""

import tkinter

Price_window = tkinter.Tk()
Price_window.geometry("1000x1500")
Price_window.title("Cambio de precios")
    
def text_changed(*args):
    p=int(tk_name.get())
    tk_name2.set(p)
    
    
tk_name=tkinter.StringVar()
tk_name.set("abcdef")
tk_name.trace("w", text_changed)
tk_name2=tkinter.StringVar()
tk_name2.set("abcdef")
tk_name2.trace("w", text_changed)

Fill_Label = tkinter.Label(Price_window, text= "        ")
Fill_Label.grid(row = 0, column = 0)
Fill_Label2 = tkinter.Label(Price_window, text= "        ")
Fill_Label2.grid(row = 0, column = 2)
    
Label_Title = tkinter.Label(Price_window, text = "        Código")
Label_Title.grid(row = 2, column = 0, columnspan = 3)
Box_textd1 = tkinter.Entry(Price_window, textvariable = tk_name)
Box_textd1.grid(row = 3, column = 1, sticky="W")
Box_textd2 = tkinter.Entry(Price_window)
Box_textd2.grid(row = 4, column = 1)
Box_textd3 = tkinter.Entry(Price_window)
Box_textd3.grid(row = 5, column = 1)
Box_textd4 = tkinter.Entry(Price_window)
Box_textd4.grid(row = 6, column = 1)
Box_textd5 = tkinter.Entry(Price_window)
Box_textd5.grid(row = 7, column = 1)
Box_textd6 = tkinter.Entry(Price_window)
Box_textd6.grid(row = 8, column = 1)
Box_textd7 = tkinter.Entry(Price_window)
Box_textd7.grid(row = 9, column = 1)
Box_textd8 = tkinter.Entry(Price_window)
Box_textd8.grid(row = 10, column = 1)
    
Label_Title2 = tkinter.Label(Price_window, text = "        Precio")
Label_Title2.grid(row = 2, column = 3, columnspan = 3)
Box_text1 = tkinter.Entry(Price_window, textvariable = tk_name2)
Box_text1.grid(row = 3, column = 3)
Box_text2 = tkinter.Entry(Price_window)
Box_text2.grid(row = 4, column = 3)
Box_text3 = tkinter.Entry(Price_window)
Box_text3.grid(row = 5, column = 3)
Box_text4 = tkinter.Entry(Price_window)
Box_text4.grid(row = 6, column = 3)
Box_text5 = tkinter.Entry(Price_window)
Box_text5.grid(row = 7, column = 3)
Box_text6 = tkinter.Entry(Price_window)
Box_text6.grid(row = 8, column = 3)
Box_text7 = tkinter.Entry(Price_window)
Box_text7.grid(row = 9, column = 3)
Box_text8 = tkinter.Entry(Price_window)
Box_text8.grid(row = 10, column = 3)
    
    
Price_window.mainloop()