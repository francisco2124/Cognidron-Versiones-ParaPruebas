from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.capturarObservaciones import Ui_capturarObservaciones
from PyQt5.QtGui import QIntValidator



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_Observaciones(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de capturar observaciones")
        self.ui= Ui_capturarObservaciones()
        self.ui.setupUi(self)
        #self.idTerapeuta = idTerapeuta
        self.InicializarGui()


    def InicializarGui(self):
        print("Hola mundo :)")
