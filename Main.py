# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:54:15 2021

@author: emili
"""
from Daily import day
from Price import price
import tkinter 

import subprocess


def Dia():
    day()   
    
def Precio():
    retcode = subprocess.call(["K.exe"])
    

main_window = tkinter.Tk()
main_window.geometry('600x600')
main_window.title("Miguel Angel")


Title = tkinter.Label(main_window, text = "Menu Principal")
Title.config(font =("Courier", 20))
Title.pack()

DayBotton = tkinter.Button(main_window, text="Planilla Diaria", command = Dia)
DayBotton.pack()

PriceBotton = tkinter.Button(main_window, text="Cambiar precios", command = Precio)
PriceBotton.pack()

main_window.mainloop()


