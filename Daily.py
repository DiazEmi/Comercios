# -*- coding: utf-8 -*-
"""
agregar proteccion para cuando apreten 2 veces el boton de finalizar
"""


import tkinter
import pymongo
from datetime import datetime
from datetime import date

hora = datetime.now()
today = date.today() 


client = pymongo.MongoClient("mongodb+srv://yo:yolo@cluster0.0mjgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["Negocio"]
mycol = mydb["diario"]

if hora.hour <= 15:
    turno = 'mañana'
else:
    turno = 'tarde'

Day_window = tkinter.Tk()
Day_window.geometry("800x700")
Day_window.title("Planilla Diaria " + str(today))

list_cuentas=[" ", "Option 1", "Option 2", "Option 3", "Option 4"]
list_empleados=[" ", "Option 1", "Option 2", "Option 3", "Option 4"]
list_gastos=[" ", "Option 1", "Option 2", "Option 3", "Option 4"]
list_cajeros=[" ", "Option 1", "Option 2", "Option 3", "Option 4"]

var_cuentas=[]

Label_Title1 = tkinter.Label(Day_window, text = "                 Cuentas Corrientes")
Label_Title1.grid(row = 0, column = 0, columnspan = 3)
Label_Name = tkinter.Label(Day_window, text = "Nombre de la cuenta corriente  ")
Label_Name.grid(row = 1, column = 0)
Label_Amount= tkinter.Label(Day_window, text = "Monto")
Label_Amount.grid(row = 1, column = 1)

var_cobros=[]
var_montos_cobros=[]

for i in range(6):
    var = tkinter.StringVar(Day_window)
    var.set(" ")
    var_cobros.append(var)
    name_list =tkinter.OptionMenu(Day_window, var_cobros[i], *list_cuentas)
    name_list.grid(row=2+i,column=0)
    var2 = tkinter.Entry(Day_window)
    var_montos_cobros.append(var2)
    var2.grid(row = 2+i, column = 1)
    
    
    
    
Label_Title2 = tkinter.Label(Day_window, text = "            Pago de Cuentas Corrientes")
Label_Title2.grid(row = 9, column = 0, columnspan = 3)
Label_Name = tkinter.Label(Day_window, text = "Nombre de la cuenta corriente  ")
Label_Name.grid(row = 10, column = 0)
Label_Amount= tkinter.Label(Day_window, text = "Monto")
Label_Amount.grid(row = 10, column = 1)


var_pagos=[]
var_montos_pagos=[]

for i in range(6):
    var = tkinter.StringVar(Day_window)
    var.set(" ")
    var_pagos.append(var)
    name_list =tkinter.OptionMenu(Day_window, var_pagos[i], *list_cuentas)
    name_list.grid(row=11+i,column=0)
    var2 = tkinter.Entry(Day_window)
    var_montos_pagos.append(var2)
    var2.grid(row = 11+i, column = 1)
    

Label_Title1 = tkinter.Label(Day_window, text = "                 Pagos        ")
Label_Title1.grid(row = 0, column = 4, columnspan = 3)
Label_NameG = tkinter.Label(Day_window, text = "Nombre")
Label_NameG.grid(row = 1, column = 4)
Label_Amount= tkinter.Label(Day_window, text = "Monto")
Label_Amount.grid(row = 1, column = 5)


var_gastos=[]
var_monto_gastos=[]



for i in range(6):
    var = tkinter.StringVar(Day_window)
    var.set(' ')
    var_gastos.append(var)
    name_list =tkinter.OptionMenu(Day_window, var_gastos[i], *list_gastos)
    name_list.grid(row=2+i,column=4)
    var2 = tkinter.Entry(Day_window)
    var_monto_gastos.append(var2)
    var2.grid(row = 2+i, column = 5)



Label_Title1 = tkinter.Label(Day_window, text = "                 Retiros empleados")
Label_Title1.grid(row = 9, column = 4, columnspan = 3)
Label_NameG = tkinter.Label(Day_window, text = "Nombre del empleado")
Label_NameG.grid(row = 10, column = 4)
Label_Amount= tkinter.Label(Day_window, text = "Monto")
Label_Amount.grid(row = 10, column = 5)

var_empleado=[]
var_montos_empleado=[]

for i in range(6):
    var = tkinter.StringVar(Day_window)
    var.set(" ")
    var_empleado.append(var)
    name_list =tkinter.OptionMenu(Day_window, var_empleado[i], *list_empleados)
    name_list.grid(row=11+i,column=4)
    var2 = tkinter.Entry(Day_window)
    var_montos_empleado.append(var2)
    var2.grid(row = 11+i, column = 5)  


Label_Amount= tkinter.Label(Day_window, text = "Cajero")
Label_Amount.grid(row = 22, column = 3)
varca = tkinter.StringVar(Day_window)
varca.set(' ')
name_list_ca = tkinter.OptionMenu(Day_window, varca, *list_cajeros)
name_list_ca.grid(row = 22, column = 4)




Label_Title2 = tkinter.Label(Day_window, text = "            Debitos")
Label_Title2.grid(row = 18, column = 0, columnspan = 3)
Box_textd1 = tkinter.Entry(Day_window)
Box_textd1.grid(row = 19, column = 1)
Box_textd2 = tkinter.Entry(Day_window)
Box_textd2.grid(row = 20, column = 1)
Box_textd3 = tkinter.Entry(Day_window)
Box_textd3.grid(row = 21, column = 1)
Box_textd4 = tkinter.Entry(Day_window)
Box_textd4.grid(row = 22, column = 1)


Label_Title2 = tkinter.Label(Day_window, text = "   Efectivo")
Label_Title2.grid(row = 19, column = 2, columnspan = 3)
Box_textc1 = tkinter.Entry(Day_window)
Box_textc1.grid(row = 20, column = 4)
    
spacer = tkinter.Label(Day_window, text = "                      ")
spacer.grid(row = 20, column = 2)    

    

def Update():
    total=0
    cajero = varca.get()
    dic={}
    if Box_textd1.get()!='':
        debi1=int(Box_textd1.get())
    else:
        debi1=0
    if Box_textd2.get()!='':
        debi2=int(Box_textd2.get())
    else:
        debi2=0
    if Box_textd3.get()!='':
        debi3=int(Box_textd3.get())
    else:
        debi3=0
    if Box_textd4.get()!='':
        debi4=int(Box_textd4.get())
    else:
        debi4=0
    debi = debi1 + debi2 + debi3 + debi4
    total=debi
    if Box_textc1.get()!='':
        efe=int(Box_textc1.get())
    else:
        efe=0
    total = total + efe
    iva=''
    for j in range(6):
        va = var_monto_gastos[j].get()
        if va != '':
            iva=int(va)
        else:
            iva=0
        if (iva)!=0:
            f = str(var_gastos[j].get())
            dic[f]=iva
            total = total + iva
            iva=0
    for j in range(6):
        va = var_montos_cobros[j].get()
        if va != '':
            iva=int(va)
        else:
            iva=0
        if (iva)!=0:
            dic[str(var_cobros[j].get())]=iva
            total = total + iva
            iva=0
    for j in range(6):
        va = var_montos_pagos[j].get()
        if va != '':
            iva=int(va)
        else:
            iva=0
        if (iva)!=0:
            dic[str(var_pagos[j].get())]=iva
            total = total - iva
            iva=0
    for j in range(6):
        va = var_montos_empleado[j].get()
        if va != '':
            iva=int(va)
        else:
            iva=0
        if (iva)!=0:
            dic[str(var_empleado[j].get())]=iva
            total = total + iva
            iva=0
    dic={'dia':today.day,'mes':today.month,'año':today.year,'cajero':cajero,'ventas':total,'efectivo':efe,'debitos':debi,'Turno':turno}
    print(dic)
    mycol.insert_one(dic)
    
    
    
Finish_Button = tkinter.Button(Day_window, text= "      Finalizar      ", command = Update)
Finish_Button.grid(row =22, column = 5)
Day_window.mainloop()

#i = {'dia':today.day,'mes':today.month,'año':today.year,'Cajero':0,'Turno':turno,'preciom':0,'precioM':0,'precioB':0}
