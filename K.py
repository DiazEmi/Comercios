
import tkinter
import pymongo

client = pymongo.MongoClient("mongodb+srv://yo:yolo@cluster0.0mjgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["Negocio"]
mycol = mydb["precios"]


Price_window = tkinter.Tk()
Price_window.geometry("1000x1500")
Price_window.title("Cambio de precios")

c=[]
list_names=[]
list_unit=[]
list_cost=[]
list_menor=[]
list_mayor=[]
list_bulto=[]

item_details = mycol.find()
for item in item_details:
    c.append(item['_id'])
    list_names.append(item['nombre'])
    list_cost.append(item['precioC'])
    list_menor.append((item['preciom']))
    list_mayor.append(item['precioM'])
    list_bulto.append(item['precioB'])
    list_unit.append(item['Kg'])
    
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
            box_menor[k].set((p/f)*1.6)
            box_mayor[k].set((p/f)*1.2)
            box_bulto[k].set((p)*1.5)
            x = mycol.update_one({'_id' : c[k] }, {'$set':{'precioC':p}})

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
