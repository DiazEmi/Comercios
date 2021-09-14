# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:23:41 2021

@author: emili
"""

import tkinter


Price_window = tkinter.Tk()
Price_window.geometry("1000x1500")
Price_window.title("Cambio de precios")
list_names=['Papa blanca','Papa Negra','Papa roja','Papa lavada','Cebolla','Cebolla morada','Verdeo','Zanahoria','Zanahoria Fraccionada','Zapallito','Berenjena blanca','4','1','2','3','4']
list_unit=['20','20','20','16','18','15','1.5','13','18','25','16','12','13','14','15','16']
list_cost=['300','400','500','600','600','500','100','600','1200','1000','11','12','13','14','15','16']
list_menor=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
list_mayor=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
list_bulto=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
 
box_var = []
box_unit = []
box_menor = []
box_mayor = []
box_bulto = []
leng = len(list_names) 



def text00(*args):
    for k in range(leng):
        t=box_var[k].get()
        if t == '':
            t=0
        p=float(t)
        f=float(list_cost[k])
        if p != f:
            print(str(p)+ "++" + str(f))
            list_cost[k]=p
            f=float(box_unit[k].get())
            box_menor[k].set((p/f)*1.6  )

for i in range(leng):
    var = tkinter.StringVar()
    var.set(list_cost[i])
    var.trace("w", text00)
    box_var.append(var)
    Box_textd1 = tkinter.Entry(Price_window, textvariable = box_var[i], width=10)
    Box_textd1.grid(row = i+1, column = 1, sticky="W")


for i in range(leng):
    var = tkinter.StringVar()
    var.set(list_unit[i])
    var.trace("w", text00)
    box_unit.append(var)
    Box_textd1 = tkinter.Entry(Price_window, textvariable = box_unit[i], width=10)
    Box_textd1.grid(row = i+1, column = 2, sticky="W")

for i in range(leng):
    var = tkinter.StringVar()
    var.set(list_menor[i])
    var.trace("w", text00)
    box_menor.append(var)
    Box_textd1 = tkinter.Entry(Price_window, textvariable = box_menor[i], width=10)
    Box_textd1.grid(row = i+1, column = 3, sticky="W")

for i in range(leng):
    var = tkinter.StringVar()
    var.set(list_mayor[i])
    var.trace("w", text00)
    box_mayor.append(var)
    Box_textd1 = tkinter.Entry(Price_window, textvariable = box_mayor[i], width=10)
    Box_textd1.grid(row = i+1, column = 4, sticky="W")

for i in range(leng):
    var = tkinter.StringVar()
    var.set(list_bulto[i])
    var.trace("w", text00)
    box_bulto.append(var)
    Box_textd1 = tkinter.Entry(Price_window, textvariable = box_bulto[i], width=10)
    Box_textd1.grid(row = i+1, column = 5, sticky="W")
    
Label_Title = tkinter.Label(Price_window, text = "   Producto")
Label_Title.grid(row = 0, column = 0)
Label_Title = tkinter.Label(Price_window, text = "   P. comp")
Label_Title.grid(row = 0, column = 1)
Label_Title = tkinter.Label(Price_window, text = "   Kg / U")
Label_Title.grid(row = 0, column = 2)
Label_Title = tkinter.Label(Price_window, text = "   P menor")
Label_Title.grid(row = 0, column = 3)
Label_Title = tkinter.Label(Price_window, text = "   P mayor")
Label_Title.grid(row = 0, column = 4)
Label_Title = tkinter.Label(Price_window, text = "   P bulto")
Label_Title.grid(row = 0, column = 5)





#Box_textd1 = tkinter.Entry(Price_window, textvariable = tk_name00)
#Box_textd1.grid(row = 1, column = 1, sticky="W")
    
for k in range(leng):
    
    Label_Title = tkinter.Label(Price_window, text = list_names[k])
    Label_Title.grid(row = k+1, column = 0)
    
Price_window.mainloop()
