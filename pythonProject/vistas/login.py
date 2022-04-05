# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images.images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 551)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(410, 552))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/idea-genial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 111))
        self.frame.setStyleSheet("background-color: rgb(232, 228, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 0, 281, 81))
        self.label_2.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 60, 151, 51))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("image: url(:/newPrefix/idea-genial.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 110, 431, 441))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnIngresar = QtWidgets.QPushButton(self.frame_2)
        self.btnIngresar.setGeometry(QtCore.QRect(150, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:244, stop:0.00497512 rgba(187, 185, 180, 255), stop:0.16 rgba(234, 233, 230, 255), stop:0.225 rgba(212, 206, 181, 255), stop:0.39801 rgba(204, 201, 183, 255), stop:0.552239 rgba(235, 231, 203, 255), stop:0.695 rgba(202, 197, 176, 255), stop:0.88 rgba(203, 209, 204, 255), stop:1 rgba(178, 178, 178, 255));")
        self.btnIngresar.setObjectName("btnIngresar")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 31, 31))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("image: url(:/newPrefix/padlock.png);\n"
"background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 31, 31))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("image: url(:/newPrefix/user.png);\n"
"background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 151, 51))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));\n"
"font: 75 10pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 170, 151, 31))
        self.label_5.setStyleSheet("background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));\n"
"font: 75 10pt \"Times New Roman\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.etUser = QtWidgets.QLineEdit(self.frame_2)
        self.etUser.setGeometry(QtCore.QRect(60, 90, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.etUser.setFont(font)
        self.etUser.setAutoFillBackground(False)
        self.etUser.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 226, 255);")
        self.etUser.setObjectName("etUser")
        self.etPass = QtWidgets.QLineEdit(self.frame_2)
        self.etPass.setGeometry(QtCore.QRect(60, 210, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.etPass.setFont(font)
        self.etPass.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 226, 255);")
        self.etPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.etPass.setObjectName("etPass")
        self.btnVerPas = QtWidgets.QPushButton(self.frame_2)
        self.btnVerPas.setGeometry(QtCore.QRect(350, 220, 31, 31))
        self.btnVerPas.setStyleSheet("background-color: qconicalgradient(cx:0.488, cy:0.494318, angle:123.4, stop:0 rgba(0, 0, 0, 0));\n"
"border-image: url(:/newPrefix/vision.png);")
        self.btnVerPas.setText("")
        self.btnVerPas.setObjectName("btnVerPas")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(-20, 0, 461, 10))
        self.lineEdit.setObjectName("lineEdit")
        self.btnOlvideMiPass = QtWidgets.QCommandLinkButton(self.frame_2)
        self.btnOlvideMiPass.setGeometry(QtCore.QRect(90, 390, 241, 31))
        self.btnOlvideMiPass.setStyleSheet("font: 9pt \"Times New Roman\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOlvideMiPass.setIcon(icon1)
        self.btnOlvideMiPass.setObjectName("btnOlvideMiPass")
        self.actionUsuario = QtWidgets.QAction(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUsuario.setIcon(icon2)
        self.actionUsuario.setObjectName("actionUsuario")
        self.actionUsuario_2 = QtWidgets.QAction(Dialog)
        self.actionUsuario_2.setIcon(icon2)
        self.actionUsuario_2.setObjectName("actionUsuario_2")
        self.actionUsuario_3 = QtWidgets.QAction(Dialog)
        self.actionUsuario_3.setIcon(icon2)
        self.actionUsuario_3.setObjectName("actionUsuario_3")
        self.actionUsuario_4 = QtWidgets.QAction(Dialog)
        self.actionUsuario_4.setIcon(icon2)
        self.actionUsuario_4.setObjectName("actionUsuario_4")
        self.actionkk = QtWidgets.QAction(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/idea-genial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionkk.setIcon(icon3)
        self.actionkk.setObjectName("actionkk")
        self.actionkk_2 = QtWidgets.QAction(Dialog)
        self.actionkk_2.setIcon(icon3)
        self.actionkk_2.setObjectName("actionkk_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cognidron_EEG"))
        self.label_2.setText(_translate("Dialog", "CogniDron-EEG"))
        self.label.setText(_translate("Dialog", "Ingresa tus credenciales"))
        self.btnIngresar.setText(_translate("Dialog", "Ingresar"))
        self.label_8.setToolTip(_translate("Dialog", "Ingresa solo letras y numeros sin espacios"))
        self.label_7.setToolTip(_translate("Dialog", "Ingresa solo letras y numeros sin espacios"))
        self.label_4.setText(_translate("Dialog", "Nombre de usuario"))
        self.label_5.setText(_translate("Dialog", "Contraseña"))
        self.etUser.setPlaceholderText(_translate("Dialog", "Ingresa tu usuario"))
        self.etPass.setPlaceholderText(_translate("Dialog", "Ingresa tu contraseña"))
        self.btnOlvideMiPass.setText(_translate("Dialog", "¿olvidaste tu usuario o contraseña?"))
        self.actionUsuario.setText(_translate("Dialog", "Usuario"))
        self.actionUsuario.setToolTip(_translate("Dialog", "Ingresa usuario solo con alphanumerico"))
        self.actionUsuario_2.setText(_translate("Dialog", "Usuario"))
        self.actionUsuario_2.setToolTip(_translate("Dialog", "Ingresa usuario solo con alphanumerico"))
        self.actionUsuario_3.setText(_translate("Dialog", "Usuario"))
        self.actionUsuario_3.setToolTip(_translate("Dialog", "Ingresa usuario solo con alphanumerico"))
        self.actionUsuario_4.setText(_translate("Dialog", "Usuario"))
        self.actionUsuario_4.setToolTip(_translate("Dialog", "Ingresa usuario solo con alphanumerico"))
        self.actionkk.setText(_translate("Dialog", "kk"))
        self.actionkk_2.setText(_translate("Dialog", "kk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

