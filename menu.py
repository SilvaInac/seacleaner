# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camera = QVideoWidget(self.groupBox_3)
        self.camera.setMinimumSize(QtCore.QSize(300, 200))
        self.camera.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.camera.setObjectName("camera")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.camera)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2.addWidget(self.camera)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startDrone = QtWidgets.QPushButton(self.groupBox)
        self.startDrone.setObjectName("startDrone")
        self.horizontalLayout_3.addWidget(self.startDrone)
        self.stopDrone = QtWidgets.QPushButton(self.groupBox)
        self.stopDrone.setObjectName("stopDrone")
        self.horizontalLayout_3.addWidget(self.stopDrone)
        self.captureDrone = QtWidgets.QPushButton(self.groupBox)
        self.captureDrone.setObjectName("captureDrone")
        self.horizontalLayout_3.addWidget(self.captureDrone)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.op_group = QtWidgets.QGroupBox(self.frame_2)
        self.op_group.setMinimumSize(QtCore.QSize(125, 150))
        self.op_group.setMaximumSize(QtCore.QSize(16777215, 200))
        self.op_group.setObjectName("op_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.op_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.op_group)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.op_group)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.op_group)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.op_group)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.op_group)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.op_group)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.op_group)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.op_group)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.op_group)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.op_group)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 4, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.op_group)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.op_group)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(125, 150))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.refreshButton = QtWidgets.QPushButton(self.groupBox_2)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout_4.addWidget(self.refreshButton)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpera_o = QtWidgets.QAction(MainWindow)
        self.actionOpera_o.setObjectName("actionOpera_o")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSimula_o = QtWidgets.QAction(MainWindow)
        self.actionSimula_o.setObjectName("actionSimula_o")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionPerfil = QtWidgets.QAction(MainWindow)
        self.actionPerfil.setObjectName("actionPerfil")
        self.menuMenu.addAction(self.actionOpera_o)
        self.menuMenu.addAction(self.actionPerfil)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSimula_o)
        self.menuHelp.addAction(self.actionSobre)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Detection"))
        self.groupBox.setTitle(_translate("MainWindow", "Drone Commands"))
        self.startDrone.setText(_translate("MainWindow", "Start"))
        self.stopDrone.setText(_translate("MainWindow", "Stop"))
        self.captureDrone.setText(_translate("MainWindow", "Capture"))
        self.op_group.setTitle(_translate("MainWindow", "Skimmers OP"))
        self.label_11.setText(_translate("MainWindow", "ON"))
        self.label_13.setText(_translate("MainWindow", "30min"))
        self.label_15.setText(_translate("MainWindow", "150min"))
        self.label_16.setText(_translate("MainWindow", "Quantity:"))
        self.label_10.setText(_translate("MainWindow", "Status:"))
        self.label_12.setText(_translate("MainWindow", "TF:"))
        self.label_17.setText(_translate("MainWindow", "5"))
        self.label_14.setText(_translate("MainWindow", "TL:"))
        self.label_18.setText(_translate("MainWindow", "Types:"))
        self.label_19.setText(_translate("MainWindow", "1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Drone"))
        self.label_3.setText(_translate("MainWindow", "ON"))
        self.label_6.setText(_translate("MainWindow", "Resolution:"))
        self.label_5.setText(_translate("MainWindow", "15min"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.label_4.setText(_translate("MainWindow", "Time:"))
        self.label_7.setText(_translate("MainWindow", "720p"))
        self.label_8.setText(_translate("MainWindow", "Altura:"))
        self.label_9.setText(_translate("MainWindow", "13M"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpera_o.setText(_translate("MainWindow", "Operation"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimula_o.setText(_translate("MainWindow", "Simulação"))
        self.actionSobre.setText(_translate("MainWindow", "About"))
        self.actionPerfil.setText(_translate("MainWindow", "Perfil"))
from PyQt5.QtMultimediaWidgets import QVideoWidget