# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ui_files\FormProductGroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormProductGroup(object):
    def setupUi(self, FormProductGroup):
        FormProductGroup.setObjectName("FormProductGroup")
        FormProductGroup.resize(559, 466)
        self.list_main = QtWidgets.QListWidget(FormProductGroup)
        self.list_main.setGeometry(QtCore.QRect(50, 60, 181, 301))
        self.list_main.setAlternatingRowColors(True)
        self.list_main.setObjectName("list_main")
        self.list_second = QtWidgets.QListWidget(FormProductGroup)
        self.list_second.setGeometry(QtCore.QRect(330, 60, 181, 301))
        self.list_second.setObjectName("list_second")
        self.btn_addMain = QtWidgets.QPushButton(FormProductGroup)
        self.btn_addMain.setGeometry(QtCore.QRect(50, 370, 51, 41))
        self.btn_addMain.setObjectName("btn_addMain")
        self.btn_editMain = QtWidgets.QPushButton(FormProductGroup)
        self.btn_editMain.setGeometry(QtCore.QRect(110, 370, 51, 41))
        self.btn_editMain.setObjectName("btn_editMain")
        self.btn_deleteMain = QtWidgets.QPushButton(FormProductGroup)
        self.btn_deleteMain.setGeometry(QtCore.QRect(190, 370, 41, 41))
        self.btn_deleteMain.setObjectName("btn_deleteMain")
        self.btn_addSecond = QtWidgets.QPushButton(FormProductGroup)
        self.btn_addSecond.setGeometry(QtCore.QRect(330, 370, 51, 41))
        self.btn_addSecond.setObjectName("btn_addSecond")
        self.btn_deleteSecond = QtWidgets.QPushButton(FormProductGroup)
        self.btn_deleteSecond.setGeometry(QtCore.QRect(470, 370, 41, 41))
        self.btn_deleteSecond.setObjectName("btn_deleteSecond")
        self.btn_editSecond = QtWidgets.QPushButton(FormProductGroup)
        self.btn_editSecond.setGeometry(QtCore.QRect(390, 370, 51, 41))
        self.btn_editSecond.setObjectName("btn_editSecond")
        self.label = QtWidgets.QLabel(FormProductGroup)
        self.label.setGeometry(QtCore.QRect(50, 26, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormProductGroup)
        self.label_2.setGeometry(QtCore.QRect(330, 26, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FormProductGroup)
        QtCore.QMetaObject.connectSlotsByName(FormProductGroup)

    def retranslateUi(self, FormProductGroup):
        _translate = QtCore.QCoreApplication.translate
        FormProductGroup.setWindowTitle(_translate("FormProductGroup", "Form"))
        self.btn_addMain.setText(_translate("FormProductGroup", "Ekle"))
        self.btn_editMain.setText(_translate("FormProductGroup", "Düzenle"))
        self.btn_deleteMain.setText(_translate("FormProductGroup", "Sil"))
        self.btn_addSecond.setText(_translate("FormProductGroup", "Ekle"))
        self.btn_deleteSecond.setText(_translate("FormProductGroup", "Sil"))
        self.btn_editSecond.setText(_translate("FormProductGroup", "Düzenle"))
        self.label.setText(_translate("FormProductGroup", "Üst Grup"))
        self.label_2.setText(_translate("FormProductGroup", "Alt Grup"))