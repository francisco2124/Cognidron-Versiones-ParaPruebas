# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principalCognitronp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 907)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/idea-genial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(33, 33))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setEnabled(True)
        self.mdiArea.setGeometry(QtCore.QRect(10, 20, 1261, 810))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setMinimumSize(QtCore.QSize(1200, 810))
        self.mdiArea.setBaseSize(QtCore.QSize(800, 800))
        self.mdiArea.setStyleSheet("")
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 26))
        self.menubar.setObjectName("menubar")
        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuAchivo = QtWidgets.QMenu(self.menubar)
        self.menuAchivo.setObjectName("menuAchivo")
        self.opc_Paciente = QtWidgets.QMenu(self.menuAchivo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/paciente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opc_Paciente.setIcon(icon1)
        self.opc_Paciente.setObjectName("opc_Paciente")
        self.menuTutor = QtWidgets.QMenu(self.menuAchivo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/familia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTutor.setIcon(icon2)
        self.menuTutor.setObjectName("menuTutor")
        self.menuTerapeuta = QtWidgets.QMenu(self.menuAchivo)
        self.menuTerapeuta.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/terapeuta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTerapeuta.setIcon(icon3)
        self.menuTerapeuta.setObjectName("menuTerapeuta")
        self.menuEjercicios = QtWidgets.QMenu(self.menubar)
        self.menuEjercicios.setObjectName("menuEjercicios")
        self.menuNeurofeedback = QtWidgets.QMenu(self.menuEjercicios)
        self.menuNeurofeedback.setObjectName("menuNeurofeedback")
        self.menuModo_Libre = QtWidgets.QMenu(self.menuEjercicios)
        self.menuModo_Libre.setObjectName("menuModo_Libre")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuCoexion = QtWidgets.QMenu(self.menubar)
        self.menuCoexion.setObjectName("menuCoexion")
        self.menuConectar_Robot_Fisico = QtWidgets.QMenu(self.menuCoexion)
        self.menuConectar_Robot_Fisico.setObjectName("menuConectar_Robot_Fisico")
        self.menuConectar_con_Diadema = QtWidgets.QMenu(self.menuCoexion)
        self.menuConectar_con_Diadema.setObjectName("menuConectar_con_Diadema")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("background-color: rgb(159, 182, 206);")
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.mni_cascada = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_cascada.setIcon(icon4)
        self.mni_cascada.setObjectName("mni_cascada")
        self.mni_cuadricula = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/cuadricula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_cuadricula.setIcon(icon5)
        self.mni_cuadricula.setObjectName("mni_cuadricula")
        self.mni_subven = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/ventana.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mni_subven.setIcon(icon6)
        self.mni_subven.setObjectName("mni_subven")
        self.actionElevar_Drone_2 = QtWidgets.QAction(MainWindow)
        self.actionElevar_Drone_2.setObjectName("actionElevar_Drone_2")
        self.actionMnatener_Drone = QtWidgets.QAction(MainWindow)
        self.actionMnatener_Drone.setObjectName("actionMnatener_Drone")
        self.actionBajar_Drono = QtWidgets.QAction(MainWindow)
        self.actionBajar_Drono.setObjectName("actionBajar_Drono")
        self.actionMover_a_la_derecha = QtWidgets.QAction(MainWindow)
        self.actionMover_a_la_derecha.setObjectName("actionMover_a_la_derecha")
        self.actionMover_a_la_isquierda = QtWidgets.QAction(MainWindow)
        self.actionMover_a_la_isquierda.setObjectName("actionMover_a_la_isquierda")
        self.actionLevel_1 = QtWidgets.QAction(MainWindow)
        self.actionLevel_1.setObjectName("actionLevel_1")
        self.actionLevel_2 = QtWidgets.QAction(MainWindow)
        self.actionLevel_2.setObjectName("actionLevel_2")
        self.actionLevel_3 = QtWidgets.QAction(MainWindow)
        self.actionLevel_3.setObjectName("actionLevel_3")
        self.actionLevel_4 = QtWidgets.QAction(MainWindow)
        self.actionLevel_4.setObjectName("actionLevel_4")
        self.actionLevel_5 = QtWidgets.QAction(MainWindow)
        self.actionLevel_5.setObjectName("actionLevel_5")
        self.menuCrear_Paciente = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCrear_Paciente.setIcon(icon7)
        self.menuCrear_Paciente.setObjectName("menuCrear_Paciente")
        self.actionConsultar_Paciente = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConsultar_Paciente.setIcon(icon8)
        self.actionConsultar_Paciente.setObjectName("actionConsultar_Paciente")
        self.actionCrear_Tutor_2 = QtWidgets.QAction(MainWindow)
        self.actionCrear_Tutor_2.setIcon(icon7)
        self.actionCrear_Tutor_2.setObjectName("actionCrear_Tutor_2")
        self.actionConsultar_Tutor = QtWidgets.QAction(MainWindow)
        self.actionConsultar_Tutor.setIcon(icon8)
        self.actionConsultar_Tutor.setObjectName("actionConsultar_Tutor")
        self.actionCrear_Terapeutta = QtWidgets.QAction(MainWindow)
        self.actionCrear_Terapeutta.setIcon(icon7)
        self.actionCrear_Terapeutta.setObjectName("actionCrear_Terapeutta")
        self.actionConsultar_Terapeuta = QtWidgets.QAction(MainWindow)
        self.actionConsultar_Terapeuta.setIcon(icon8)
        self.actionConsultar_Terapeuta.setObjectName("actionConsultar_Terapeuta")
        self.actionIconAbrirReporte = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIconAbrirReporte.setIcon(icon9)
        self.actionIconAbrirReporte.setObjectName("actionIconAbrirReporte")
        self.actionVistaCuadricula = QtWidgets.QAction(MainWindow)
        self.actionVistaCuadricula.setIcon(icon5)
        self.actionVistaCuadricula.setObjectName("actionVistaCuadricula")
        self.actionBotonDetener = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/detener.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBotonDetener.setIcon(icon10)
        self.actionBotonDetener.setObjectName("actionBotonDetener")
        self.actionIconoTutor = QtWidgets.QAction(MainWindow)
        self.actionIconoTutor.setIcon(icon2)
        self.actionIconoTutor.setObjectName("actionIconoTutor")
        self.actionIconoTerapia = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/salud-mental.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIconoTerapia.setIcon(icon11)
        self.actionIconoTerapia.setObjectName("actionIconoTerapia")
        self.actionIconLibro = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/libro-abierto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIconLibro.setIcon(icon12)
        self.actionIconLibro.setObjectName("actionIconLibro")
        self.actionVistaCascada = QtWidgets.QAction(MainWindow)
        self.actionVistaCascada.setIcon(icon4)
        self.actionVistaCascada.setObjectName("actionVistaCascada")
        self.actionIconPaciente = QtWidgets.QAction(MainWindow)
        self.actionIconPaciente.setIcon(icon1)
        self.actionIconPaciente.setObjectName("actionIconPaciente")
        self.actionBotonPausa = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/pausa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBotonPausa.setIcon(icon13)
        self.actionBotonPausa.setObjectName("actionBotonPausa")
        self.actionBotonPlay = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBotonPlay.setIcon(icon14)
        self.actionBotonPlay.setObjectName("actionBotonPlay")
        self.actionBotonEncender = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/poder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBotonEncender.setIcon(icon15)
        self.actionBotonEncender.setObjectName("actionBotonEncender")
        self.actionIconConsulatrReporte = QtWidgets.QAction(MainWindow)
        self.actionIconConsulatrReporte.setIcon(icon12)
        self.actionIconConsulatrReporte.setObjectName("actionIconConsulatrReporte")
        self.actionIconoTerapia_2 = QtWidgets.QAction(MainWindow)
        self.actionIconoTerapia_2.setIcon(icon)
        self.actionIconoTerapia_2.setObjectName("actionIconoTerapia_2")
        self.actionIconoTerapeuta = QtWidgets.QAction(MainWindow)
        self.actionIconoTerapeuta.setIcon(icon3)
        self.actionIconoTerapeuta.setObjectName("actionIconoTerapeuta")
        self.actionIconoConexion = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/newPrefix/wifi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIconoConexion.setIcon(icon16)
        self.actionIconoConexion.setObjectName("actionIconoConexion")
        self.actionDrone = QtWidgets.QAction(MainWindow)
        self.actionDrone.setObjectName("actionDrone")
        self.actionRobot_Lego = QtWidgets.QAction(MainWindow)
        self.actionRobot_Lego.setObjectName("actionRobot_Lego")
        self.actionConsultar_Reporte = QtWidgets.QAction(MainWindow)
        self.actionConsultar_Reporte.setIcon(icon12)
        self.actionConsultar_Reporte.setObjectName("actionConsultar_Reporte")
        self.actionEditar_Reporte = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/newPrefix/reporte.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditar_Reporte.setIcon(icon17)
        self.actionEditar_Reporte.setObjectName("actionEditar_Reporte")
        self.actionVistaVentana = QtWidgets.QAction(MainWindow)
        self.actionVistaVentana.setIcon(icon6)
        self.actionVistaVentana.setObjectName("actionVistaVentana")
        self.actionConfigurar_parametros_de_conexi_n = QtWidgets.QAction(MainWindow)
        self.actionConfigurar_parametros_de_conexi_n.setObjectName("actionConfigurar_parametros_de_conexi_n")
        self.actiontutor = QtWidgets.QAction(MainWindow)
        self.actiontutor.setIcon(icon2)
        self.actiontutor.setObjectName("actiontutor")
        self.mni_tabs = QtWidgets.QAction(MainWindow)
        self.mni_tabs.setObjectName("mni_tabs")
        self.actionConectar_Emotiv = QtWidgets.QAction(MainWindow)
        self.actionConectar_Emotiv.setObjectName("actionConectar_Emotiv")
        self.menuVista.addAction(self.mni_cascada)
        self.menuVista.addAction(self.mni_cuadricula)
        self.menuVista.addAction(self.mni_tabs)
        self.opc_Paciente.addSeparator()
        self.opc_Paciente.addAction(self.menuCrear_Paciente)
        self.opc_Paciente.addAction(self.actionConsultar_Paciente)
        self.menuTutor.addAction(self.actionCrear_Tutor_2)
        self.menuTutor.addAction(self.actionConsultar_Tutor)
        self.menuTerapeuta.addAction(self.actionCrear_Terapeutta)
        self.menuTerapeuta.addAction(self.actionConsultar_Terapeuta)
        self.menuAchivo.addAction(self.menuTerapeuta.menuAction())
        self.menuAchivo.addAction(self.menuTutor.menuAction())
        self.menuAchivo.addAction(self.opc_Paciente.menuAction())
        self.menuNeurofeedback.addAction(self.actionElevar_Drone_2)
        self.menuNeurofeedback.addAction(self.actionMnatener_Drone)
        self.menuNeurofeedback.addAction(self.actionBajar_Drono)
        self.menuNeurofeedback.addAction(self.actionMover_a_la_derecha)
        self.menuNeurofeedback.addAction(self.actionMover_a_la_isquierda)
        self.menuModo_Libre.addAction(self.actionLevel_1)
        self.menuModo_Libre.addAction(self.actionLevel_2)
        self.menuModo_Libre.addAction(self.actionLevel_3)
        self.menuModo_Libre.addAction(self.actionLevel_4)
        self.menuModo_Libre.addAction(self.actionLevel_5)
        self.menuEjercicios.addAction(self.menuNeurofeedback.menuAction())
        self.menuEjercicios.addAction(self.menuModo_Libre.menuAction())
        self.menuConectar_Robot_Fisico.addAction(self.actionDrone)
        self.menuConectar_Robot_Fisico.addAction(self.actionRobot_Lego)
        self.menuConectar_con_Diadema.addAction(self.actionConectar_Emotiv)
        self.menuCoexion.addAction(self.menuConectar_con_Diadema.menuAction())
        self.menuCoexion.addAction(self.menuConectar_Robot_Fisico.menuAction())
        self.menuCoexion.addAction(self.actionConfigurar_parametros_de_conexi_n)
        self.menuReportes.addAction(self.actionConsultar_Reporte)
        self.menuReportes.addAction(self.actionEditar_Reporte)
        self.menubar.addAction(self.menuAchivo.menuAction())
        self.menubar.addAction(self.menuEjercicios.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuCoexion.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionIconAbrirReporte)
        self.toolBar.addAction(self.actionIconConsulatrReporte)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionIconoTerapeuta)
        self.toolBar.addAction(self.actionIconoTutor)
        self.toolBar.addAction(self.actionIconPaciente)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionIconoConexion)
        self.toolBar.addAction(self.actionIconoTerapia)
        self.toolBar.addAction(self.actionIconoTerapia_2)
        self.toolBar.addAction(self.actionIconLibro)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionVistaCuadricula)
        self.toolBar.addAction(self.actionVistaCascada)
        self.toolBar.addAction(self.actionVistaVentana)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cognitron"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.menuAchivo.setTitle(_translate("MainWindow", "Achivo"))
        self.opc_Paciente.setTitle(_translate("MainWindow", "Paciente"))
        self.menuTutor.setTitle(_translate("MainWindow", "Tutor"))
        self.menuTerapeuta.setTitle(_translate("MainWindow", "Terapeuta"))
        self.menuEjercicios.setTitle(_translate("MainWindow", "Ejercicios"))
        self.menuNeurofeedback.setTitle(_translate("MainWindow", "Neurofeedback"))
        self.menuModo_Libre.setTitle(_translate("MainWindow", "Modo Libre"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuCoexion.setTitle(_translate("MainWindow", "Conexión"))
        self.menuConectar_Robot_Fisico.setTitle(_translate("MainWindow", "Conectar Robot Fisico"))
        self.menuConectar_con_Diadema.setTitle(_translate("MainWindow", "Conectar con Diadema"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.mni_cascada.setText(_translate("MainWindow", "Vista Cascada"))
        self.mni_cuadricula.setText(_translate("MainWindow", "Vista Cuadricula"))
        self.mni_subven.setText(_translate("MainWindow", "Vista Subventanas"))
        self.actionElevar_Drone_2.setText(_translate("MainWindow", "Elevar Drone"))
        self.actionMnatener_Drone.setText(_translate("MainWindow", "Mnatener Drone "))
        self.actionBajar_Drono.setText(_translate("MainWindow", "Bajar Drone"))
        self.actionMover_a_la_derecha.setText(_translate("MainWindow", "Mover a la derecha"))
        self.actionMover_a_la_isquierda.setText(_translate("MainWindow", "Mover a la isquierda"))
        self.actionLevel_1.setText(_translate("MainWindow", "Level 1"))
        self.actionLevel_2.setText(_translate("MainWindow", "Level 2"))
        self.actionLevel_3.setText(_translate("MainWindow", "Level 3"))
        self.actionLevel_4.setText(_translate("MainWindow", "Level 4"))
        self.actionLevel_5.setText(_translate("MainWindow", "Level 5"))
        self.menuCrear_Paciente.setText(_translate("MainWindow", "Crear Paciente"))
        self.actionConsultar_Paciente.setText(_translate("MainWindow", "Consultar Paciente"))
        self.actionCrear_Tutor_2.setText(_translate("MainWindow", "Crear Tutor"))
        self.actionConsultar_Tutor.setText(_translate("MainWindow", "Consultar Tutor"))
        self.actionCrear_Terapeutta.setText(_translate("MainWindow", "Crear Terapeutta"))
        self.actionConsultar_Terapeuta.setText(_translate("MainWindow", "Consultar Terapeuta"))
        self.actionIconAbrirReporte.setText(_translate("MainWindow", "IconAbrirReporte"))
        self.actionIconAbrirReporte.setToolTip(_translate("MainWindow", "Abrir Reporte"))
        self.actionIconAbrirReporte.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionVistaCuadricula.setText(_translate("MainWindow", "VistaCuadricula"))
        self.actionVistaCuadricula.setToolTip(_translate("MainWindow", "Vista Cuadricula"))
        self.actionVistaCuadricula.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionBotonDetener.setText(_translate("MainWindow", "BotonDetener"))
        self.actionBotonDetener.setToolTip(_translate("MainWindow", "Detener"))
        self.actionIconoTutor.setText(_translate("MainWindow", "IconoTutor"))
        self.actionIconoTutor.setToolTip(_translate("MainWindow", "Consultar Tutor"))
        self.actionIconoTutor.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionIconoTerapia.setText(_translate("MainWindow", "IconoOndas"))
        self.actionIconoTerapia.setToolTip(_translate("MainWindow", "Mostar Ondas Cerebrales"))
        self.actionIconoTerapia.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionIconLibro.setText(_translate("MainWindow", "IconEjercicos"))
        self.actionIconLibro.setToolTip(_translate("MainWindow", "Abrir Ejercicos"))
        self.actionIconLibro.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionVistaCascada.setText(_translate("MainWindow", "VistaCascada"))
        self.actionVistaCascada.setToolTip(_translate("MainWindow", "Vista Cascada"))
        self.actionVistaCascada.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionIconPaciente.setText(_translate("MainWindow", "IconPaciente"))
        self.actionIconPaciente.setToolTip(_translate("MainWindow", "Consultar Paciente"))
        self.actionIconPaciente.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionBotonPausa.setText(_translate("MainWindow", "BotonPausa"))
        self.actionBotonPausa.setToolTip(_translate("MainWindow", "Pausar"))
        self.actionBotonPlay.setText(_translate("MainWindow", "BotonPlay"))
        self.actionBotonPlay.setToolTip(_translate("MainWindow", "Play"))
        self.actionBotonEncender.setText(_translate("MainWindow", "BotonEncender"))
        self.actionBotonEncender.setToolTip(_translate("MainWindow", "Iniciar"))
        self.actionIconConsulatrReporte.setText(_translate("MainWindow", "IconConsulatrReporte"))
        self.actionIconConsulatrReporte.setToolTip(_translate("MainWindow", "Consultar Reportes"))
        self.actionIconConsulatrReporte.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionIconoTerapia_2.setText(_translate("MainWindow", "IconoTerapia"))
        self.actionIconoTerapia_2.setToolTip(_translate("MainWindow", "Abrir Terapa"))
        self.actionIconoTerapia_2.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionIconoTerapeuta.setText(_translate("MainWindow", "IconoTerapeuta"))
        self.actionIconoTerapeuta.setToolTip(_translate("MainWindow", "Consulatr Terapeutas"))
        self.actionIconoTerapeuta.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionIconoConexion.setText(_translate("MainWindow", "IconoConexion"))
        self.actionIconoConexion.setToolTip(_translate("MainWindow", "Conexion"))
        self.actionIconoConexion.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionDrone.setText(_translate("MainWindow", "Drone"))
        self.actionRobot_Lego.setText(_translate("MainWindow", "Robot Lego"))
        self.actionConsultar_Reporte.setText(_translate("MainWindow", "Consultar Reporte"))
        self.actionEditar_Reporte.setText(_translate("MainWindow", "Editar Reporte"))
        self.actionVistaVentana.setText(_translate("MainWindow", "VistaVentana"))
        self.actionVistaVentana.setToolTip(_translate("MainWindow", "Vista Ventanas"))
        self.actionVistaVentana.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionConfigurar_parametros_de_conexi_n.setText(_translate("MainWindow", "Configurar parametros de conexión"))
        self.actiontutor.setText(_translate("MainWindow", "tutor"))
        self.actiontutor.setToolTip(_translate("MainWindow", "Consultar_Tutor"))
        self.mni_tabs.setText(_translate("MainWindow", "Vista Pestaña"))
        self.actionConectar_Emotiv.setText(_translate("MainWindow", "Conectar Emotiv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

