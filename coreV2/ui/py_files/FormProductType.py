# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ui_files\FormProductType.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormProductType(object):
    def setupUi(self, FormProductType):
        FormProductType.setObjectName("FormProductType")
        FormProductType.resize(596, 658)
        self.table_productTypes = QtWidgets.QTableWidget(FormProductType)
        self.table_productTypes.setGeometry(QtCore.QRect(20, 210, 561, 371))
        self.table_productTypes.setAlternatingRowColors(True)
        self.table_productTypes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_productTypes.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_productTypes.setObjectName("table_productTypes")
        self.table_productTypes.setColumnCount(0)
        self.table_productTypes.setRowCount(0)
        self.btn_add = QtWidgets.QPushButton(FormProductType)
        self.btn_add.setGeometry(QtCore.QRect(460, 20, 121, 31))
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(FormProductType)
        self.btn_edit.setGeometry(QtCore.QRect(460, 60, 121, 31))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtWidgets.QPushButton(FormProductType)
        self.btn_delete.setGeometry(QtCore.QRect(460, 140, 121, 31))
        self.btn_delete.setObjectName("btn_delete")
        self.gb_search = QtWidgets.QGroupBox(FormProductType)
        self.gb_search.setGeometry(QtCore.QRect(20, 10, 431, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gb_search.setFont(font)
        self.gb_search.setObjectName("gb_search")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.gb_search)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(19, 19, 391, 141))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_productCode = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productCode.setFont(font)
        self.lbl_productCode.setObjectName("lbl_productCode")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_productCode)
        self.txt_productType = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txt_productType.setObjectName("txt_productType")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_productType)
        self.lbl_productMainGroup = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productMainGroup.setFont(font)
        self.lbl_productMainGroup.setObjectName("lbl_productMainGroup")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_productMainGroup)
        self.cb_mainCat = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.cb_mainCat.setObjectName("cb_mainCat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_mainCat)
        self.lbl_productSecondGroup = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productSecondGroup.setFont(font)
        self.lbl_productSecondGroup.setObjectName("lbl_productSecondGroup")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_productSecondGroup)
        self.cb_secondaryCat = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.cb_secondaryCat.setObjectName("cb_secondaryCat")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_secondaryCat)
        self.lbl_productSecondGroup_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productSecondGroup_2.setFont(font)
        self.lbl_productSecondGroup_2.setObjectName("lbl_productSecondGroup_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_productSecondGroup_2)
        self.cb_status = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.cb_status.setObjectName("cb_status")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_status)
        self.btn_list = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_list.setFont(font)
        self.btn_list.setObjectName("btn_list")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btn_list)
        self.label = QtWidgets.QLabel(FormProductType)
        self.label.setGeometry(QtCore.QRect(30, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_records = QtWidgets.QLabel(FormProductType)
        self.lbl_records.setGeometry(QtCore.QRect(130, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_records.setFont(font)
        self.lbl_records.setText("")
        self.lbl_records.setObjectName("lbl_records")
        self.lbl_amount = QtWidgets.QLabel(FormProductType)
        self.lbl_amount.setGeometry(QtCore.QRect(440, 590, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_amount.setFont(font)
        self.lbl_amount.setText("")
        self.lbl_amount.setObjectName("lbl_amount")
        self.btn_refreshFilters = QtWidgets.QPushButton(FormProductType)
        self.btn_refreshFilters.setGeometry(QtCore.QRect(20, 180, 91, 25))
        self.btn_refreshFilters.setObjectName("btn_refreshFilters")
        self.lbl_filters = QtWidgets.QLabel(FormProductType)
        self.lbl_filters.setGeometry(QtCore.QRect(126, 180, 455, 25))
        self.lbl_filters.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_filters.setObjectName("lbl_filters")
        self.btn_excel = QtWidgets.QPushButton(FormProductType)
        self.btn_excel.setGeometry(QtCore.QRect(471, 630, 111, 21))
        self.btn_excel.setObjectName("btn_excel")
        self.btn_print = QtWidgets.QPushButton(FormProductType)
        self.btn_print.setGeometry(QtCore.QRect(340, 630, 118, 21))
        self.btn_print.setObjectName("btn_print")
        self.btn_refresh = QtWidgets.QPushButton(FormProductType)
        self.btn_refresh.setGeometry(QtCore.QRect(460, 100, 121, 31))
        self.btn_refresh.setObjectName("btn_refresh")

        self.retranslateUi(FormProductType)
        QtCore.QMetaObject.connectSlotsByName(FormProductType)

    def retranslateUi(self, FormProductType):
        _translate = QtCore.QCoreApplication.translate
        FormProductType.setWindowTitle(_translate("FormProductType", "Form"))
        self.table_productTypes.setSortingEnabled(True)
        self.btn_add.setText(_translate("FormProductType", "Yeni Kayıt"))
        self.btn_edit.setText(_translate("FormProductType", "Düzenle"))
        self.btn_delete.setText(_translate("FormProductType", "Sil"))
        self.gb_search.setTitle(_translate("FormProductType", "Arama"))
        self.lbl_productCode.setText(_translate("FormProductType", "Malzeme Cins :"))
        self.lbl_productMainGroup.setText(_translate("FormProductType", "Üst Grup :"))
        self.lbl_productSecondGroup.setText(_translate("FormProductType", "Alt Grup :"))
        self.lbl_productSecondGroup_2.setText(_translate("FormProductType", "Durum :"))
        self.btn_list.setText(_translate("FormProductType", "Listele"))
        self.label.setText(_translate("FormProductType", "Toplam Kayıt :"))
        self.btn_refreshFilters.setText(_translate("FormProductType", "Sıfırla"))
        self.lbl_filters.setText(_translate("FormProductType", "Filtre Seçilmedi."))
        self.btn_excel.setText(_translate("FormProductType", "Excel ile Dışarı Aktar"))
        self.btn_print.setText(_translate("FormProductType", "Print"))
        self.btn_refresh.setText(_translate("FormProductType", "Yenile"))
