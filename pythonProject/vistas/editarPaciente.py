# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarPaciente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditarPaciente(object):
    def setupUi(self, EditarPaciente):
        EditarPaciente.setObjectName("EditarPaciente")
        EditarPaciente.resize(508, 631)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/terapeuta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditarPaciente.setWindowIcon(icon)
        self.leLocalidad = QtWidgets.QLineEdit(EditarPaciente)
        self.leLocalidad.setGeometry(QtCore.QRect(190, 410, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLocalidad.setFont(font)
        self.leLocalidad.setMaxLength(28)
        self.leLocalidad.setObjectName("leLocalidad")
        self.label_16 = QtWidgets.QLabel(EditarPaciente)
        self.label_16.setGeometry(QtCore.QRect(20, 530, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.cbEstado = QtWidgets.QComboBox(EditarPaciente)
        self.cbEstado.setGeometry(QtCore.QRect(190, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbEstado.setFont(font)
        self.cbEstado.setObjectName("cbEstado")
        self.cbEstado.addItem("")
        self.leApeMaterno = QtWidgets.QLineEdit(EditarPaciente)
        self.leApeMaterno.setGeometry(QtCore.QRect(190, 140, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApeMaterno.setFont(font)
        self.leApeMaterno.setMaxLength(28)
        self.leApeMaterno.setObjectName("leApeMaterno")
        self.leCalle = QtWidgets.QLineEdit(EditarPaciente)
        self.leCalle.setGeometry(QtCore.QRect(190, 440, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCalle.setFont(font)
        self.leCalle.setMaxLength(30)
        self.leCalle.setObjectName("leCalle")
        self.label_6 = QtWidgets.QLabel(EditarPaciente)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(EditarPaciente)
        self.label_10.setGeometry(QtCore.QRect(20, 410, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(EditarPaciente)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.leNacionalidad = QtWidgets.QLineEdit(EditarPaciente)
        self.leNacionalidad.setGeometry(QtCore.QRect(190, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNacionalidad.setFont(font)
        self.leNacionalidad.setMaxLength(28)
        self.leNacionalidad.setObjectName("leNacionalidad")
        self.label_5 = QtWidgets.QLabel(EditarPaciente)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.leCorreoElectronico = QtWidgets.QLineEdit(EditarPaciente)
        self.leCorreoElectronico.setGeometry(QtCore.QRect(190, 530, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCorreoElectronico.setFont(font)
        self.leCorreoElectronico.setText("")
        self.leCorreoElectronico.setMaxLength(30)
        self.leCorreoElectronico.setObjectName("leCorreoElectronico")
        self.label_13 = QtWidgets.QLabel(EditarPaciente)
        self.label_13.setGeometry(QtCore.QRect(20, 470, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(EditarPaciente)
        self.label_17.setGeometry(QtCore.QRect(20, 530, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.cbMunicipio = QtWidgets.QComboBox(EditarPaciente)
        self.cbMunicipio.setGeometry(QtCore.QRect(190, 380, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbMunicipio.setFont(font)
        self.cbMunicipio.setObjectName("cbMunicipio")
        self.cbMunicipio.addItem("")
        self.label_11 = QtWidgets.QLabel(EditarPaciente)
        self.label_11.setGeometry(QtCore.QRect(20, 440, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.leCodigoPostal = QtWidgets.QLineEdit(EditarPaciente)
        self.leCodigoPostal.setGeometry(QtCore.QRect(190, 470, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCodigoPostal.setFont(font)
        self.leCodigoPostal.setMaxLength(5)
        self.leCodigoPostal.setObjectName("leCodigoPostal")
        self.label_18 = QtWidgets.QLabel(EditarPaciente)
        self.label_18.setGeometry(QtCore.QRect(20, 320, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_9 = QtWidgets.QLabel(EditarPaciente)
        self.label_9.setGeometry(QtCore.QRect(20, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.leNombre = QtWidgets.QLineEdit(EditarPaciente)
        self.leNombre.setGeometry(QtCore.QRect(190, 170, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNombre.setFont(font)
        self.leNombre.setMaxLength(28)
        self.leNombre.setObjectName("leNombre")
        self.leApePaterno = QtWidgets.QLineEdit(EditarPaciente)
        self.leApePaterno.setGeometry(QtCore.QRect(190, 110, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApePaterno.setFont(font)
        self.leApePaterno.setMaxLength(28)
        self.leApePaterno.setObjectName("leApePaterno")
        self.label_3 = QtWidgets.QLabel(EditarPaciente)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leNumeroContacto = QtWidgets.QLineEdit(EditarPaciente)
        self.leNumeroContacto.setGeometry(QtCore.QRect(190, 500, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumeroContacto.setFont(font)
        self.leNumeroContacto.setMaxLength(10)
        self.leNumeroContacto.setObjectName("leNumeroContacto")
        self.label_14 = QtWidgets.QLabel(EditarPaciente)
        self.label_14.setGeometry(QtCore.QRect(20, 500, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(EditarPaciente)
        self.label_12.setGeometry(QtCore.QRect(20, 380, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(EditarPaciente)
        self.label_15.setGeometry(QtCore.QRect(20, 210, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_2 = QtWidgets.QLabel(EditarPaciente)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.leNumero = QtWidgets.QLineEdit(EditarPaciente)
        self.leNumero.setGeometry(QtCore.QRect(320, 440, 51, 21))
        self.leNumero.setMaxLength(4)
        self.leNumero.setObjectName("leNumero")
        self.btnAceptar = QtWidgets.QPushButton(EditarPaciente)
        self.btnAceptar.setGeometry(QtCore.QRect(230, 570, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnCancelar = QtWidgets.QPushButton(EditarPaciente)
        self.btnCancelar.setGeometry(QtCore.QRect(340, 570, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.groupBox = QtWidgets.QGroupBox(EditarPaciente)
        self.groupBox.setGeometry(QtCore.QRect(180, 200, 221, 51))
        self.groupBox.setObjectName("groupBox")
        self.rbFemenino = QtWidgets.QRadioButton(self.groupBox)
        self.rbFemenino.setGeometry(QtCore.QRect(120, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbFemenino.setFont(font)
        self.rbFemenino.setChecked(True)
        self.rbFemenino.setObjectName("rbFemenino")
        self.rbMasculino = QtWidgets.QRadioButton(self.groupBox)
        self.rbMasculino.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbMasculino.setFont(font)
        self.rbMasculino.setChecked(False)
        self.rbMasculino.setObjectName("rbMasculino")
        self.dateEdit = QtWidgets.QDateEdit(EditarPaciente)
        self.dateEdit.setGeometry(QtCore.QRect(190, 260, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2002, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.frame_2 = QtWidgets.QFrame(EditarPaciente)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 521, 8))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 8))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(EditarPaciente)
        self.frame.setGeometry(QtCore.QRect(0, 0, 521, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(430, 10, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/paciente.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(EditarPaciente)
        self.label_25.setGeometry(QtCore.QRect(0, 70, 531, 641))
        self.label_25.setMinimumSize(QtCore.QSize(100, 100))
        self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_19 = QtWidgets.QLabel(EditarPaciente)
        self.label_19.setGeometry(QtCore.QRect(20, 290, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.cbEstado_2 = QtWidgets.QComboBox(EditarPaciente)
        self.cbEstado_2.setGeometry(QtCore.QRect(190, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbEstado_2.setFont(font)
        self.cbEstado_2.setObjectName("cbEstado_2")
        self.cbEstado_2.addItem("")
        self.label_25.raise_()
        self.leLocalidad.raise_()
        self.label_16.raise_()
        self.cbEstado.raise_()
        self.leApeMaterno.raise_()
        self.leCalle.raise_()
        self.label_6.raise_()
        self.label_10.raise_()
        self.label_4.raise_()
        self.leNacionalidad.raise_()
        self.label_5.raise_()
        self.leCorreoElectronico.raise_()
        self.label_13.raise_()
        self.label_17.raise_()
        self.cbMunicipio.raise_()
        self.label_11.raise_()
        self.leCodigoPostal.raise_()
        self.label_18.raise_()
        self.label_9.raise_()
        self.leNombre.raise_()
        self.leApePaterno.raise_()
        self.label_3.raise_()
        self.leNumeroContacto.raise_()
        self.label_14.raise_()
        self.label_12.raise_()
        self.label_15.raise_()
        self.label_2.raise_()
        self.leNumero.raise_()
        self.btnAceptar.raise_()
        self.btnCancelar.raise_()
        self.groupBox.raise_()
        self.dateEdit.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_19.raise_()
        self.cbEstado_2.raise_()

        self.retranslateUi(EditarPaciente)
        QtCore.QMetaObject.connectSlotsByName(EditarPaciente)

    def retranslateUi(self, EditarPaciente):
        _translate = QtCore.QCoreApplication.translate
        EditarPaciente.setWindowTitle(_translate("EditarPaciente", "Editar Terapeuta"))
        self.label_16.setText(_translate("EditarPaciente", "Correo electrónico"))
        self.cbEstado.setItemText(0, _translate("EditarPaciente", "Jalisco"))
        self.label_10.setText(_translate("EditarPaciente", "Localidad"))
        self.label_4.setText(_translate("EditarPaciente", "Nombre"))
        self.label_5.setText(_translate("EditarPaciente", "Fecha de nacimiento"))
        self.label_13.setText(_translate("EditarPaciente", "Código postal"))
        self.cbMunicipio.setItemText(0, _translate("EditarPaciente", "Ameca"))
        self.label_11.setText(_translate("EditarPaciente", "Calle y número"))
        self.label_18.setText(_translate("EditarPaciente", "Nacionalidad"))
        self.label_9.setText(_translate("EditarPaciente", "Estado"))
        self.label_3.setText(_translate("EditarPaciente", "Apellido Materno"))
        self.label_14.setText(_translate("EditarPaciente", "Número de contacto"))
        self.label_12.setText(_translate("EditarPaciente", "Municipio"))
        self.label_15.setText(_translate("EditarPaciente", "Genero"))
        self.label_2.setText(_translate("EditarPaciente", "Apellido paterno"))
        self.btnAceptar.setText(_translate("EditarPaciente", "Editar"))
        self.btnCancelar.setText(_translate("EditarPaciente", "Limpiar Campos"))
        self.groupBox.setTitle(_translate("EditarPaciente", "Seleciona una opción"))
        self.rbFemenino.setText(_translate("EditarPaciente", "Femenino"))
        self.rbMasculino.setText(_translate("EditarPaciente", "Masculino"))
        self.label_8.setText(_translate("EditarPaciente", "Modificar datos del Paciente"))
        self.label_19.setText(_translate("EditarPaciente", "Tutor"))
        self.cbEstado_2.setItemText(0, _translate("EditarPaciente", "Sin_Tutor"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarPaciente = QtWidgets.QDialog()
    ui = Ui_EditarPaciente()
    ui.setupUi(EditarPaciente)
    EditarPaciente.show()
    sys.exit(app.exec_())
