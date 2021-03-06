# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Op.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Op(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 425)
        Dialog.setMaximumSize(QtCore.QSize(608, 426))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setStyleSheet("image: url(:/s/s-multiplasEscovas.jpg);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setStyleSheet("image: url(:/s/s-seasw.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 1, 2, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 1, 3, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setStyleSheet("image: url(:/s/s-tambor.jpg);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setStyleSheet("image: url(:/s/s-weir.webp);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(590, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.op_group = QtWidgets.QGroupBox(self.groupBox_2)
        self.op_group.setGeometry(QtCore.QRect(10, 20, 130, 171))
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
        self.op_group_2 = QtWidgets.QGroupBox(self.groupBox_2)
        self.op_group_2.setGeometry(QtCore.QRect(160, 20, 130, 171))
        self.op_group_2.setMinimumSize(QtCore.QSize(125, 150))
        self.op_group_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.op_group_2.setObjectName("op_group_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.op_group_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_26 = QtWidgets.QLabel(self.op_group_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.op_group_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.op_group_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.op_group_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.op_group_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.op_group_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.op_group_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.op_group_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.op_group_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.op_group_3.setGeometry(QtCore.QRect(320, 20, 255, 171))
        self.op_group_3.setMinimumSize(QtCore.QSize(255, 150))
        self.op_group_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.op_group_3.setObjectName("op_group_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.op_group_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_30 = QtWidgets.QLabel(self.op_group_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.op_group_3)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.op_group_3)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 2, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.op_group_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 3, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.op_group_3)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.op_group_3)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 1, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.op_group_3)
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 3, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.op_group_3)
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 2, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.op_group_3)
        self.label_38.setObjectName("label_38")
        self.gridLayout_4.addWidget(self.label_38, 4, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.op_group_3)
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.op_group_3)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        self.spinBox.valueChanged['QString'].connect(self.label_20.setText)
        self.spinBox_2.valueChanged['QString'].connect(self.label_21.setText)
        self.spinBox_3.valueChanged['QString'].connect(self.label_22.setText)
        self.spinBox_4.valueChanged['QString'].connect(self.label_26.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Skimmers"))
        self.groupBox_2.setTitle(_translate("Dialog", "Info"))
        self.op_group.setTitle(_translate("Dialog", "Skimmers OP"))
        self.label_11.setText(_translate("Dialog", "ON"))
        self.label_13.setText(_translate("Dialog", "30min"))
        self.label_15.setText(_translate("Dialog", "150min"))
        self.label_16.setText(_translate("Dialog", "Quantity:"))
        self.label_10.setText(_translate("Dialog", "Status:"))
        self.label_12.setText(_translate("Dialog", "TF:"))
        self.label_17.setText(_translate("Dialog", "5"))
        self.label_14.setText(_translate("Dialog", "TL:"))
        self.label_18.setText(_translate("Dialog", "Types:"))
        self.label_19.setText(_translate("Dialog", "1"))
        self.op_group_2.setTitle(_translate("Dialog", "Types"))
        self.label_26.setText(_translate("Dialog", "0"))
        self.label_24.setText(_translate("Dialog", "SME"))
        self.label_27.setText(_translate("Dialog", "SB"))
        self.label_25.setText(_translate("Dialog", "SR"))
        self.label_20.setText(_translate("Dialog", "0"))
        self.label_22.setText(_translate("Dialog", "0"))
        self.label_21.setText(_translate("Dialog", "0"))
        self.label_23.setText(_translate("Dialog", "SW"))
        self.op_group_3.setTitle(_translate("Dialog", "Info OP"))
        self.label_30.setText(_translate("Dialog", "1552"))
        self.label_31.setText(_translate("Dialog", "carlos.silva@inatel.br"))
        self.label_32.setText(_translate("Dialog", "Leticia Calixto"))
        self.label_33.setText(_translate("Dialog", "Team:"))
        self.label_34.setText(_translate("Dialog", "Operation ID"))
        self.label_35.setText(_translate("Dialog", "Contact"))
        self.label_36.setText(_translate("Dialog", "5"))
        self.label_37.setText(_translate("Dialog", "Operator:"))
        self.label_38.setText(_translate("Dialog", "Time:"))
        self.label_39.setText(_translate("Dialog", "1"))
        self.pushButton.setText(_translate("Dialog", "Start Skimmer"))
import Skimmers_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Op()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
