# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambiarPass.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images


class Ui_cambiarPass(object):
    def setupUi(self, cambiarPass):
        cambiarPass.setObjectName("cambiarPass")
        cambiarPass.resize(277, 287)
        cambiarPass.setMinimumSize(QtCore.QSize(100, 100))
        self.btnRegistrar_2 = QtWidgets.QPushButton(cambiarPass)
        self.btnRegistrar_2.setGeometry(QtCore.QRect(90, 210, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRegistrar_2.setFont(font)
        self.btnRegistrar_2.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.btnRegistrar_2.setObjectName("btnRegistrar_2")
        self.frame = QtWidgets.QFrame(cambiarPass)
        self.frame.setGeometry(QtCore.QRect(0, 0, 281, 51))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 271, 41))
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
        self.label_23.setStyleSheet("image: url(:/newPrefix/terapeuta.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.lePassword_2 = QtWidgets.QLineEdit(cambiarPass)
        self.lePassword_2.setGeometry(QtCore.QRect(40, 100, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lePassword_2.setFont(font)
        self.lePassword_2.setText("")
        self.lePassword_2.setMaxLength(10)
        self.lePassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword_2.setObjectName("lePassword_2")
        self.label_24 = QtWidgets.QLabel(cambiarPass)
        self.label_24.setGeometry(QtCore.QRect(60, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.leCofirnarPassword_2 = QtWidgets.QLineEdit(cambiarPass)
        self.leCofirnarPassword_2.setGeometry(QtCore.QRect(40, 170, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCofirnarPassword_2.setFont(font)
        self.leCofirnarPassword_2.setText("")
        self.leCofirnarPassword_2.setMaxLength(10)
        self.leCofirnarPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leCofirnarPassword_2.setObjectName("leCofirnarPassword_2")
        self.label_8 = QtWidgets.QLabel(cambiarPass)
        self.label_8.setGeometry(QtCore.QRect(0, 50, 381, 331))
        self.label_8.setMinimumSize(QtCore.QSize(100, 100))
        self.label_8.setStyleSheet("background-color: rgb(116, 147, 198);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_25 = QtWidgets.QLabel(cambiarPass)
        self.label_25.setGeometry(QtCore.QRect(50, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.btnVerPas_4 = QtWidgets.QPushButton(cambiarPass)
        self.btnVerPas_4.setGeometry(QtCore.QRect(230, 170, 21, 21))
        self.btnVerPas_4.setStyleSheet("background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));\n"
"border-image: url(:/newPrefix/vision.png);")
        self.btnVerPas_4.setText("")
        self.btnVerPas_4.setObjectName("btnVerPas_4")
        self.btnVerPas_3 = QtWidgets.QPushButton(cambiarPass)
        self.btnVerPas_3.setGeometry(QtCore.QRect(230, 100, 21, 21))
        self.btnVerPas_3.setStyleSheet("background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));\n"
"border-image: url(:/newPrefix/vision.png);")
        self.btnVerPas_3.setText("")
        self.btnVerPas_3.setObjectName("btnVerPas_3")
        self.frame_2 = QtWidgets.QFrame(cambiarPass)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 621, 10))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 14))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8.raise_()
        self.btnRegistrar_2.raise_()
        self.frame.raise_()
        self.lePassword_2.raise_()
        self.label_24.raise_()
        self.leCofirnarPassword_2.raise_()
        self.label_25.raise_()
        self.btnVerPas_4.raise_()
        self.btnVerPas_3.raise_()
        self.frame_2.raise_()

        self.retranslateUi(cambiarPass)
        QtCore.QMetaObject.connectSlotsByName(cambiarPass)

    def retranslateUi(self, cambiarPass):
        _translate = QtCore.QCoreApplication.translate
        cambiarPass.setWindowTitle(_translate("cambiarPass", "Dialog"))
        self.btnRegistrar_2.setText(_translate("cambiarPass", "Cambiar"))
        self.label_3.setText(_translate("cambiarPass", "Cambiar contraseña"))
        self.lePassword_2.setToolTip(_translate("cambiarPass", "La contraseña debe tener entre 6 y 10 digitos, 1 numero, una minuscula y una mayuscula"))
        self.label_24.setText(_translate("cambiarPass", "Contraseña nueva"))
        self.leCofirnarPassword_2.setToolTip(_translate("cambiarPass", "La contraseña debe tener entre 6 y 10 digitos, 1 numero, una minuscula y una mayuscula"))
        self.label_25.setText(_translate("cambiarPass", "Confirmar contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cambiarPass = QtWidgets.QDialog()
    ui = Ui_cambiarPass()
    ui.setupUi(cambiarPass)
    cambiarPass.show()
    sys.exit(app.exec_())

