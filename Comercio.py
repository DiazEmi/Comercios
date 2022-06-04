import pymongo
from datetime import datetime
from datetime import date
from plantilla import * 



class Comercio(QtWidgets.QDialog, Ui_Dialog):  
    hora = datetime.now()
    today = date.today() 
    fecha = str(hora.month)+":"+str(hora.year)
    fecha_gasto = str(fecha) + ":gastos"
    client = pymongo.MongoClient("mongodb+srv://yo:yolo@cluster0.0mjgl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = client["Negocio"]
    mycol = mydb["diario"]
    empleadoscol = mydb["empleados"]
    mynewcol = mydb[fecha]
    col_gastos = mydb[fecha_gasto]
    col_cliente = mydb["cuentas corrientes"]
    colCliente = mydb["cliente"]
    colGasto = mydb["gastos"]
    
    listEmpleado = ['']
    listCajero = ['']
    listCliente = ['']
    listGasto = ['']
    listCategoria = ['','Cuenta Corriente','Cajero','Repositor','Cajero-Repositor']
    
    
    item_details = empleadoscol.find()
    for item in item_details:
        listEmpleado.append(item['nombre'])
        if item['caja']=='S':
            listCajero.append(item['nombre'])
            
    item_details = colCliente.find()
    for item in item_details:
        listCliente.append(item['nombre'])
    
    item_details = colGasto.find()
    for item in item_details:
        listGasto.append(item['nombre'])
    
    listCajero.sort()
    listEmpleado.sort()
    listCliente.sort()
    listGasto.sort()
    cantidad = len(listEmpleado)-1
    print(listEmpleado)
    
    if hora.hour <= 15:
        turno = 'mañana'
    else:
        turno = 'tarde'
        
        
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.cmbCajero.addItems(self.listCajero)
        
        self.cmbEmpleado1.addItems(self.listEmpleado)
        self.cmbEmpleado2.addItems(self.listEmpleado)
        self.cmbEmpleado3.addItems(self.listEmpleado)
        self.cmbEmpleado4.addItems(self.listEmpleado)
        self.cmbEmpleado5.addItems(self.listEmpleado)
        self.cmbEmpleado6.addItems(self.listEmpleado)
        
        self.cmbCobros1.addItems(self.listCliente)
        self.cmbCobros2.addItems(self.listCliente)
        self.cmbCobros3.addItems(self.listCliente)
        self.cmbCobros4.addItems(self.listCliente)
        self.cmbCobros5.addItems(self.listCliente)
        self.cmbCobros6.addItems(self.listCliente)
        
        self.cmbCuentas1.addItems(self.listCliente)
        self.cmbCuentas2.addItems(self.listCliente)
        self.cmbCuentas3.addItems(self.listCliente)
        self.cmbCuentas4.addItems(self.listCliente)
        self.cmbCuentas5.addItems(self.listCliente)
        self.cmbCuentas6.addItems(self.listCliente)
        
        self.cmbGastos1.addItems(self.listGasto)
        self.cmbGastos2.addItems(self.listGasto)
        self.cmbGastos3.addItems(self.listGasto)
        self.cmbGastos4.addItems(self.listGasto)
        self.cmbGastos5.addItems(self.listGasto)
        self.cmbGastos6.addItems(self.listGasto)
        
        self.cmbDatos1.addItems(self.listCategoria)
        self.cmbDatos2.addItems(self.listCategoria)
        self.cmbDatos3.addItems(self.listCategoria)
        self.cmbDatos4.addItems(self.listCategoria)
        
        if self.cantidad >= 1:
            self.txtFranco1.setText(str(self.listEmpleado[1]))
        if self.cantidad >= 2:
            self.txtFranco2.setText(str(self.listEmpleado[2]))
        if self.cantidad >= 3:
            self.txtFranco3.setText(str(self.listEmpleado[3]))
        if self.cantidad >= 4:
            self.txtFranco4.setText(str(self.listEmpleado[4]))
        if self.cantidad >= 5:
            self.txtFranco5.setText(str(self.listEmpleado[5]))
        if self.cantidad >= 6:
            self.txtFranco6.setText(str(self.listEmpleado[6]))
        if self.cantidad >= 7:
            self.txtFranco7.setText(str(self.listEmpleado[7]))
        if self.cantidad >= 8:
            self.txtFranco8.setText(str(self.listEmpleado[8]))
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dlg = Comercio()
    dlg.show()
    app.exec_()