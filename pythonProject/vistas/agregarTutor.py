# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarTutor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_DialogAgregarTerapeuta(object):
    def setupUi(self, DialogAgregarTerapeuta):
        DialogAgregarTerapeuta.setObjectName("DialogAgregarTerapeuta")
        DialogAgregarTerapeuta.resize(490, 600)
        DialogAgregarTerapeuta.setMinimumSize(QtCore.QSize(490, 600))
        DialogAgregarTerapeuta.setMaximumSize(QtCore.QSize(490, 600))
        self.label = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label.setGeometry(QtCore.QRect(-10, 0, 551, 661))
        self.label.setMinimumSize(QtCore.QSize(480, 510))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leCorreoElectronico = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leCorreoElectronico.setGeometry(QtCore.QRect(220, 480, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCorreoElectronico.setFont(font)
        self.leCorreoElectronico.setText("")
        self.leCorreoElectronico.setMaxLength(40)
        self.leCorreoElectronico.setObjectName("leCorreoElectronico")
        self.leNombres = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leNombres.setGeometry(QtCore.QRect(220, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNombres.setFont(font)
        self.leNombres.setMaxLength(27)
        self.leNombres.setObjectName("leNombres")
        self.leCalle = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leCalle.setGeometry(QtCore.QRect(220, 390, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCalle.setFont(font)
        self.leCalle.setMaxLength(27)
        self.leCalle.setObjectName("leCalle")
        self.leLoclidad = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leLoclidad.setGeometry(QtCore.QRect(220, 360, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLoclidad.setFont(font)
        self.leLoclidad.setMaxLength(27)
        self.leLoclidad.setObjectName("leLoclidad")
        self.label_5 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_17 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_17.setGeometry(QtCore.QRect(20, 510, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_16.setGeometry(QtCore.QRect(20, 480, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_18.setGeometry(QtCore.QRect(20, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.leCodigoPostal = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leCodigoPostal.setGeometry(QtCore.QRect(220, 420, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCodigoPostal.setFont(font)
        self.leCodigoPostal.setMaxLength(5)
        self.leCodigoPostal.setObjectName("leCodigoPostal")
        self.btnCancelar = QtWidgets.QPushButton(DialogAgregarTerapeuta)
        self.btnCancelar.setGeometry(QtCore.QRect(160, 530, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("background-color: rgb(255, 211, 160);\n"
"background-color: rgb(200, 198, 223);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.leNumeroCalle = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leNumeroCalle.setGeometry(QtCore.QRect(370, 390, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumeroCalle.setFont(font)
        self.leNumeroCalle.setMaxLength(5)
        self.leNumeroCalle.setObjectName("leNumeroCalle")
        self.label_6 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.leNumeroContacto = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leNumeroContacto.setGeometry(QtCore.QRect(220, 450, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumeroContacto.setFont(font)
        self.leNumeroContacto.setMaxLength(10)
        self.leNumeroContacto.setObjectName("leNumeroContacto")
        self.btnRegistrar = QtWidgets.QPushButton(DialogAgregarTerapeuta)
        self.btnRegistrar.setGeometry(QtCore.QRect(340, 530, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label_4 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_11.setGeometry(QtCore.QRect(20, 390, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_9.setGeometry(QtCore.QRect(20, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.leApellidoPaterno = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leApellidoPaterno.setGeometry(QtCore.QRect(220, 100, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApellidoPaterno.setFont(font)
        self.leApellidoPaterno.setText("")
        self.leApellidoPaterno.setMaxLength(27)
        self.leApellidoPaterno.setDragEnabled(True)
        self.leApellidoPaterno.setObjectName("leApellidoPaterno")
        self.leApellidoMaterno = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leApellidoMaterno.setGeometry(QtCore.QRect(220, 130, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApellidoMaterno.setFont(font)
        self.leApellidoMaterno.setMaxLength(27)
        self.leApellidoMaterno.setObjectName("leApellidoMaterno")
        self.label_14 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_14.setGeometry(QtCore.QRect(20, 450, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_12.setGeometry(QtCore.QRect(20, 330, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.dateEdit = QtWidgets.QDateEdit(DialogAgregarTerapeuta)
        self.dateEdit.setGeometry(QtCore.QRect(220, 240, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1921, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1920, 9, 26), QtCore.QTime(1, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.cbEstado = QtWidgets.QComboBox(DialogAgregarTerapeuta)
        self.cbEstado.setGeometry(QtCore.QRect(220, 300, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbEstado.setFont(font)
        self.cbEstado.setObjectName("cbEstado")
        self.cbEstado.addItem("")
        self.leNacionalidad = QtWidgets.QLineEdit(DialogAgregarTerapeuta)
        self.leNacionalidad.setGeometry(QtCore.QRect(220, 270, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNacionalidad.setFont(font)
        self.leNacionalidad.setMaxLength(27)
        self.leNacionalidad.setObjectName("leNacionalidad")
        self.label_10 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_10.setGeometry(QtCore.QRect(20, 360, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_13.setGeometry(QtCore.QRect(20, 420, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(DialogAgregarTerapeuta)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbMunicipio = QtWidgets.QComboBox(DialogAgregarTerapeuta)
        self.cbMunicipio.setGeometry(QtCore.QRect(220, 330, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbMunicipio.setFont(font)
        self.cbMunicipio.setObjectName("cbMunicipio")
        self.cbMunicipio.addItem("")
        self.frame = QtWidgets.QFrame(DialogAgregarTerapeuta)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_Tutor = QtWidgets.QLabel(self.frame)
        self.label_Tutor.setGeometry(QtCore.QRect(20, 10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_Tutor.setFont(font)
        self.label_Tutor.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_Tutor.setObjectName("label_Tutor")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(410, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/familia.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.frame_2 = QtWidgets.QFrame(DialogAgregarTerapeuta)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 531, 8))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 8))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(DialogAgregarTerapeuta)
        self.groupBox.setGeometry(QtCore.QRect(220, 190, 221, 41))
        self.groupBox.setObjectName("groupBox")
        self.rbFemenino = QtWidgets.QRadioButton(self.groupBox)
        self.rbFemenino.setGeometry(QtCore.QRect(120, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbFemenino.setFont(font)
        self.rbFemenino.setObjectName("rbFemenino")
        self.rbMasculino = QtWidgets.QRadioButton(self.groupBox)
        self.rbMasculino.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbMasculino.setFont(font)
        self.rbMasculino.setObjectName("rbMasculino")

        self.retranslateUi(DialogAgregarTerapeuta)
        QtCore.QMetaObject.connectSlotsByName(DialogAgregarTerapeuta)

    def retranslateUi(self, DialogAgregarTerapeuta):
        _translate = QtCore.QCoreApplication.translate
        DialogAgregarTerapeuta.setWindowTitle(_translate("DialogAgregarTerapeuta", "Dialog"))
        self.label_3.setText(_translate("DialogAgregarTerapeuta", "Apellido materno (*)"))
        self.label_5.setText(_translate("DialogAgregarTerapeuta", "Fecha de nacimiento (*)"))
        self.label_16.setText(_translate("DialogAgregarTerapeuta", "Correo electrónico (*)"))
        self.label_18.setText(_translate("DialogAgregarTerapeuta", "Nacionalidad"))
        self.btnCancelar.setText(_translate("DialogAgregarTerapeuta", "Limpiar campos"))
        self.btnRegistrar.setText(_translate("DialogAgregarTerapeuta", "Registrar"))
        self.label_4.setText(_translate("DialogAgregarTerapeuta", "Nombre (*)"))
        self.label_11.setText(_translate("DialogAgregarTerapeuta", "Calle y número"))
        self.label_9.setText(_translate("DialogAgregarTerapeuta", "Estado"))
        self.label_15.setText(_translate("DialogAgregarTerapeuta", "Género (*)"))
        self.label_14.setText(_translate("DialogAgregarTerapeuta", "Número de contacto (*)"))
        self.label_12.setText(_translate("DialogAgregarTerapeuta", "Municipio"))
        self.cbEstado.setItemText(0, _translate("DialogAgregarTerapeuta", "Jalisco"))
        self.label_10.setText(_translate("DialogAgregarTerapeuta", "Localidad"))
        self.label_13.setText(_translate("DialogAgregarTerapeuta", "Código postal"))
        self.label_7.setText(_translate("DialogAgregarTerapeuta", "Apellido paterno (*)"))
        self.cbMunicipio.setItemText(0, _translate("DialogAgregarTerapeuta", "Ameca"))
        self.label_Tutor.setText(_translate("DialogAgregarTerapeuta", "Nuevo tutor"))
        self.groupBox.setTitle(_translate("DialogAgregarTerapeuta", "Selecciona una opción"))
        self.rbFemenino.setText(_translate("DialogAgregarTerapeuta", "Femenino"))
        self.rbMasculino.setText(_translate("DialogAgregarTerapeuta", "Masculino"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAgregarTerapeuta = QtWidgets.QDialog()
    ui = Ui_DialogAgregarTerapeuta()
    ui.setupUi(DialogAgregarTerapeuta)
    DialogAgregarTerapeuta.show()
    sys.exit(app.exec_())

