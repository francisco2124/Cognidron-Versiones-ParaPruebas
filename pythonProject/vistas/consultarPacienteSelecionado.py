# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarPacienteSelecionado.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_ConsultarPacienteSelec(object):
    def setupUi(self, ConsultarPacienteSelec):
        ConsultarPacienteSelec.setObjectName("ConsultarPacienteSelec")
        ConsultarPacienteSelec.resize(619, 807)
        self.label = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.label.setGeometry(QtCore.QRect(0, 90, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(ConsultarPacienteSelec)
        self.pushButton.setGeometry(QtCore.QRect(510, 580, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ConsultarPacienteSelec)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 660, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(ConsultarPacienteSelec)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 620, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lb1 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb1.setGeometry(QtCore.QRect(10, 150, 51, 31))
        self.lb1.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb1.setObjectName("lb1")
        self.label_4 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.label_4.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.label_4.setObjectName("label_4")
        self.lb12 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb12.setGeometry(QtCore.QRect(10, 390, 81, 31))
        self.lb12.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb12.setObjectName("lb12")
        self.lbDomicilio = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbDomicilio.setGeometry(QtCore.QRect(80, 390, 211, 31))
        self.lbDomicilio.setObjectName("lbDomicilio")
        self.lbCorreo = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbCorreo.setGeometry(QtCore.QRect(140, 470, 141, 31))
        self.lbCorreo.setObjectName("lbCorreo")
        self.lbGenero = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbGenero.setGeometry(QtCore.QRect(50, 180, 91, 31))
        self.lbGenero.setObjectName("lbGenero")
        self.lbNombre = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbNombre.setGeometry(QtCore.QRect(70, 150, 181, 31))
        self.lbNombre.setObjectName("lbNombre")
        self.lbFechaNaimiento = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbFechaNaimiento.setGeometry(QtCore.QRect(130, 210, 111, 31))
        self.lbFechaNaimiento.setObjectName("lbFechaNaimiento")
        self.lbLocalida = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbLocalida.setGeometry(QtCore.QRect(80, 360, 71, 31))
        self.lbLocalida.setObjectName("lbLocalida")
        self.lLocalidad = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lLocalidad.setGeometry(QtCore.QRect(10, 360, 71, 31))
        self.lLocalidad.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lLocalidad.setObjectName("lLocalidad")
        self.label_8 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.label_8.setGeometry(QtCore.QRect(0, 90, 621, 711))
        self.label_8.setMinimumSize(QtCore.QSize(100, 100))
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(ConsultarPacienteSelec)
        self.frame.setGeometry(QtCore.QRect(0, 0, 621, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(540, 10, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/paciente.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.tabla_pacientes = QtWidgets.QTableWidget(ConsultarPacienteSelec)
        self.tabla_pacientes.setGeometry(QtCore.QRect(20, 580, 481, 211))
        self.tabla_pacientes.setMinimumSize(QtCore.QSize(10, 10))
        self.tabla_pacientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabla_pacientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_pacientes.setDragEnabled(False)
        self.tabla_pacientes.setRowCount(0)
        self.tabla_pacientes.setColumnCount(6)
        self.tabla_pacientes.setObjectName("tabla_pacientes")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_pacientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_pacientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_pacientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_pacientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_pacientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tabla_pacientes.setHorizontalHeaderItem(5, item)
        self.frame_2 = QtWidgets.QFrame(ConsultarPacienteSelec)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 621, 10))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 14))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lb9 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb9.setGeometry(QtCore.QRect(10, 300, 141, 31))
        self.lb9.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb9.setObjectName("lb9")
        self.lb10 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb10.setGeometry(QtCore.QRect(10, 330, 141, 31))
        self.lb10.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb10.setObjectName("lb10")
        self.lb8_2 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb8_2.setGeometry(QtCore.QRect(10, 270, 141, 31))
        self.lb8_2.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb8_2.setObjectName("lb8_2")
        self.lb13 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb13.setGeometry(QtCore.QRect(10, 420, 91, 20))
        self.lb13.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb13.setObjectName("lb13")
        self.lb14 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb14.setGeometry(QtCore.QRect(10, 470, 151, 31))
        self.lb14.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb14.setObjectName("lb14")
        self.lbEdad = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbEdad.setGeometry(QtCore.QRect(50, 240, 71, 31))
        self.lbEdad.setObjectName("lbEdad")
        self.lbEstado = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbEstado.setGeometry(QtCore.QRect(60, 300, 171, 31))
        self.lbEstado.setObjectName("lbEstado")
        self.lbNacionalidad = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbNacionalidad.setGeometry(QtCore.QRect(100, 270, 91, 31))
        self.lbNacionalidad.setObjectName("lbNacionalidad")
        self.lbMunicipio = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbMunicipio.setGeometry(QtCore.QRect(80, 330, 171, 31))
        self.lbMunicipio.setObjectName("lbMunicipio")
        self.lb8 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb8.setGeometry(QtCore.QRect(10, 240, 51, 31))
        self.lb8.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb8.setObjectName("lb8")
        self.label_2 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.label_2.setGeometry(QtCore.QRect(20, 530, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbUsuario = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbUsuario.setGeometry(QtCore.QRect(170, 90, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbUsuario.setFont(font)
        self.lbUsuario.setObjectName("lbUsuario")
        self.lbContacto = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbContacto.setGeometry(QtCore.QRect(110, 420, 81, 20))
        self.lbContacto.setStyleSheet("")
        self.lbContacto.setObjectName("lbContacto")
        self.lb14_2 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb14_2.setGeometry(QtCore.QRect(10, 440, 91, 31))
        self.lb14_2.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb14_2.setObjectName("lb14_2")
        self.lbCodPostal = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbCodPostal.setGeometry(QtCore.QRect(80, 440, 141, 31))
        self.lbCodPostal.setObjectName("lbCodPostal")
        self.lbgen = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbgen.setGeometry(QtCore.QRect(10, 180, 41, 31))
        self.lbgen.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lbgen.setObjectName("lbgen")
        self.lb1_2 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb1_2.setGeometry(QtCore.QRect(290, 180, 151, 31))
        self.lb1_2.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb1_2.setObjectName("lb1_2")
        self.etfDiagnostico = QtWidgets.QTextBrowser(ConsultarPacienteSelec)
        self.etfDiagnostico.setEnabled(False)
        self.etfDiagnostico.setGeometry(QtCore.QRect(290, 220, 311, 211))
        self.etfDiagnostico.setObjectName("etfDiagnostico")
        self.lb14_3 = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lb14_3.setGeometry(QtCore.QRect(290, 150, 151, 31))
        self.lb14_3.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.lb14_3.setObjectName("lb14_3")
        self.lbTutor = QtWidgets.QLabel(ConsultarPacienteSelec)
        self.lbTutor.setGeometry(QtCore.QRect(420, 150, 141, 31))
        self.lbTutor.setObjectName("lbTutor")
        self.label_8.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lb1.raise_()
        self.label_4.raise_()
        self.lb12.raise_()
        self.lbDomicilio.raise_()
        self.lbCorreo.raise_()
        self.lbGenero.raise_()
        self.lbNombre.raise_()
        self.lbFechaNaimiento.raise_()
        self.lbLocalida.raise_()
        self.lLocalidad.raise_()
        self.frame.raise_()
        self.tabla_pacientes.raise_()
        self.frame_2.raise_()
        self.lb9.raise_()
        self.lb10.raise_()
        self.lb8_2.raise_()
        self.lb13.raise_()
        self.lb14.raise_()
        self.lbEdad.raise_()
        self.lbEstado.raise_()
        self.lbNacionalidad.raise_()
        self.lbMunicipio.raise_()
        self.lb8.raise_()
        self.label_2.raise_()
        self.lbUsuario.raise_()
        self.lbContacto.raise_()
        self.lb14_2.raise_()
        self.lbCodPostal.raise_()
        self.lbgen.raise_()
        self.lb1_2.raise_()
        self.etfDiagnostico.raise_()
        self.lb14_3.raise_()
        self.lbTutor.raise_()

        self.retranslateUi(ConsultarPacienteSelec)
        QtCore.QMetaObject.connectSlotsByName(ConsultarPacienteSelec)

    def retranslateUi(self, ConsultarPacienteSelec):
        _translate = QtCore.QCoreApplication.translate
        ConsultarPacienteSelec.setWindowTitle(_translate("ConsultarPacienteSelec", "Terapeuta Selecionado"))
        self.label.setText(_translate("ConsultarPacienteSelec", "Id del Paciente:  "))
        self.pushButton.setText(_translate("ConsultarPacienteSelec", "Consultar"))
        self.pushButton_2.setText(_translate("ConsultarPacienteSelec", "Enviar"))
        self.pushButton_3.setText(_translate("ConsultarPacienteSelec", "Descargar"))
        self.lb1.setText(_translate("ConsultarPacienteSelec", "Nombre:"))
        self.label_4.setText(_translate("ConsultarPacienteSelec", "Fecha Nacimiento:"))
        self.lb12.setText(_translate("ConsultarPacienteSelec", "Domicilio:"))
        self.lbDomicilio.setText(_translate("ConsultarPacienteSelec", "xxx"))
        self.lbCorreo.setText(_translate("ConsultarPacienteSelec", "imaldeaa23@gmail.com"))
        self.lbGenero.setText(_translate("ConsultarPacienteSelec", "Masculino"))
        self.lbNombre.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lbFechaNaimiento.setText(_translate("ConsultarPacienteSelec", "xxxxxxxxxxxxx"))
        self.lbLocalida.setText(_translate("ConsultarPacienteSelec", "numero"))
        self.lLocalidad.setText(_translate("ConsultarPacienteSelec", "Localidad:"))
        self.label_3.setText(_translate("ConsultarPacienteSelec", "Datos de un Paciente"))
        item = self.tabla_pacientes.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarPacienteSelec", "Identificador"))
        item = self.tabla_pacientes.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarPacienteSelec", "Fecha"))
        item = self.tabla_pacientes.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarPacienteSelec", "Ejercicio"))
        item = self.tabla_pacientes.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarPacienteSelec", "Duración"))
        item = self.tabla_pacientes.horizontalHeaderItem(4)
        item.setText(_translate("ConsultarPacienteSelec", "Paciente"))
        item = self.tabla_pacientes.horizontalHeaderItem(5)
        item.setText(_translate("ConsultarPacienteSelec", "Terapeuta"))
        self.lb9.setText(_translate("ConsultarPacienteSelec", "Estado:"))
        self.lb10.setText(_translate("ConsultarPacienteSelec", "Municipio:"))
        self.lb8_2.setText(_translate("ConsultarPacienteSelec", "Nacionalidad:"))
        self.lb13.setText(_translate("ConsultarPacienteSelec", "Codigo postal:"))
        self.lb14.setText(_translate("ConsultarPacienteSelec", "Correo electrónico:"))
        self.lbEdad.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lbEstado.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lbNacionalidad.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lbMunicipio.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lb8.setText(_translate("ConsultarPacienteSelec", "Edad:"))
        self.label_2.setText(_translate("ConsultarPacienteSelec", "Reportes relacionados al paciente"))
        self.lbUsuario.setText(_translate("ConsultarPacienteSelec", "xxxx"))
        self.lbContacto.setText(_translate("ConsultarPacienteSelec", "xxxxxxx"))
        self.lb14_2.setText(_translate("ConsultarPacienteSelec", "Contacto:"))
        self.lbCodPostal.setText(_translate("ConsultarPacienteSelec", "567"))
        self.lbgen.setText(_translate("ConsultarPacienteSelec", "Sexo:"))
        self.lb1_2.setText(_translate("ConsultarPacienteSelec", "Motivo de las Terapias:"))
        self.etfDiagnostico.setHtml(_translate("ConsultarPacienteSelec", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Motivo de Terapias: El paciente tiene sintomas graves de trastorno de atencion e inperactividad.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tiene problemas en clase y no puede concentrarse en sus tareas.......</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lb14_3.setText(_translate("ConsultarPacienteSelec", "Tutor del paciente:"))
        self.lbTutor.setText(_translate("ConsultarPacienteSelec", "Sin_Tutor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultarPacienteSelec = QtWidgets.QDialog()
    ui = Ui_ConsultarPacienteSelec()
    ui.setupUi(ConsultarPacienteSelec)
    ConsultarPacienteSelec.show()
    sys.exit(app.exec_())
