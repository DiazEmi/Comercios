# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:23:15 2021

@author: emili
"""


import pymongo


client = pymongo.MongoClient("mongodb+srv://yo:yolo@cluster0.0mjgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


mydb = client["Negocio"]
mycol = mydb["precios"]

i = {'_id':39,'nombre':'puerro','precioC':0,'Kg':0,'preciom':0,'precioM':0,'precioB':0}

# x = mycol.update_one({'_id' : 2 }, {'$set':{'nombre':'papa colorada'}})

# x = mycol.insert_one(i)

c=[]
n=[]
pc=[]
item_details = mycol.find()
for item in item_details:
    c.append(item['_id'])
    n.append(item['nombre'])
    pc.append(item['precioC'])
print(c)
print(n)
print(pc)
    