# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\ui_files\FormStock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormStock(object):
    def setupUi(self, FormStock):
        FormStock.setObjectName("FormStock")
        FormStock.resize(1000, 662)
        self.table_stock = QtWidgets.QTableWidget(FormStock)
        self.table_stock.setGeometry(QtCore.QRect(10, 200, 981, 421))
        self.table_stock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_stock.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_stock.setAlternatingRowColors(True)
        self.table_stock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_stock.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_stock.setGridStyle(QtCore.Qt.SolidLine)
        self.table_stock.setObjectName("table_stock")
        self.table_stock.setColumnCount(0)
        self.table_stock.setRowCount(0)
        self.table_stock.horizontalHeader().setVisible(True)
        self.table_stock.verticalHeader().setVisible(False)
        self.table_stock.verticalHeader().setSortIndicatorShown(False)
        self.groupBox = QtWidgets.QGroupBox(FormStock)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 28, 251, 153))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_productCode = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productCode.setFont(font)
        self.lbl_productCode.setObjectName("lbl_productCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_productCode)
        self.lbl_productName = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productName.setFont(font)
        self.lbl_productName.setObjectName("lbl_productName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_productName)
        self.txt_productCode = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_productCode.setObjectName("txt_productCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_productCode)
        self.txt_productName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_productName.setObjectName("txt_productName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_productName)
        self.lbl_productMainGroup = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productMainGroup.setFont(font)
        self.lbl_productMainGroup.setObjectName("lbl_productMainGroup")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_productMainGroup)
        self.lbl_productSecondGroup = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_productSecondGroup.setFont(font)
        self.lbl_productSecondGroup.setObjectName("lbl_productSecondGroup")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_productSecondGroup)
        self.txt_productMainGroup = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_productMainGroup.setObjectName("txt_productMainGroup")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_productMainGroup)
        self.txt_productSecondGroup = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_productSecondGroup.setObjectName("txt_productSecondGroup")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_productSecondGroup)
        self.btn_list = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_list.setFont(font)
        self.btn_list.setObjectName("btn_list")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btn_list)
        self.gBox_Filter1 = QtWidgets.QGroupBox(FormStock)
        self.gBox_Filter1.setGeometry(QtCore.QRect(320, 10, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gBox_Filter1.setFont(font)
        self.gBox_Filter1.setObjectName("gBox_Filter1")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.gBox_Filter1)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(9, 30, 151, 51))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cb_columnFilter1 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_columnFilter1.sizePolicy().hasHeightForWidth())
        self.cb_columnFilter1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_columnFilter1.setFont(font)
        self.cb_columnFilter1.setObjectName("cb_columnFilter1")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_columnFilter1)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.cb_rowFilter1 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_rowFilter1.setFont(font)
        self.cb_rowFilter1.setObjectName("cb_rowFilter1")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_rowFilter1)
        self.gBox_Filter2 = QtWidgets.QGroupBox(FormStock)
        self.gBox_Filter2.setGeometry(QtCore.QRect(320, 100, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gBox_Filter2.setFont(font)
        self.gBox_Filter2.setObjectName("gBox_Filter2")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.gBox_Filter2)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(9, 30, 151, 51))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.cb_columnFilter2 = QtWidgets.QComboBox(self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_columnFilter2.sizePolicy().hasHeightForWidth())
        self.cb_columnFilter2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_columnFilter2.setFont(font)
        self.cb_columnFilter2.setObjectName("cb_columnFilter2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_columnFilter2)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.cb_rowFilter2 = QtWidgets.QComboBox(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_rowFilter2.setFont(font)
        self.cb_rowFilter2.setObjectName("cb_rowFilter2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_rowFilter2)
        self.gBox_displaySettings = QtWidgets.QGroupBox(FormStock)
        self.gBox_displaySettings.setGeometry(QtCore.QRect(510, 100, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gBox_displaySettings.setFont(font)
        self.gBox_displaySettings.setObjectName("gBox_displaySettings")
        self.gridLayoutWidget = QtWidgets.QWidget(self.gBox_displaySettings)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 441, 54))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_displaySettings = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_displaySettings.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_displaySettings.setObjectName("gridLayout_displaySettings")
        self.gBox_stokManageGuide = QtWidgets.QGroupBox(FormStock)
        self.gBox_stokManageGuide.setGeometry(QtCore.QRect(510, 10, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gBox_stokManageGuide.setFont(font)
        self.gBox_stokManageGuide.setObjectName("gBox_stokManageGuide")
        self.lbl_filters = QtWidgets.QLabel(FormStock)
        self.lbl_filters.setGeometry(QtCore.QRect(90, 630, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_filters.setFont(font)
        self.lbl_filters.setObjectName("lbl_filters")
        self.btn_refreshFilters = QtWidgets.QPushButton(FormStock)
        self.btn_refreshFilters.setGeometry(QtCore.QRect(10, 630, 75, 23))
        self.btn_refreshFilters.setObjectName("btn_refreshFilters")
        self.lbl_totalRecord = QtWidgets.QLabel(FormStock)
        self.lbl_totalRecord.setGeometry(QtCore.QRect(650, 630, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_totalRecord.setFont(font)
        self.lbl_totalRecord.setObjectName("lbl_totalRecord")
        self.lbl_totalAmount = QtWidgets.QLabel(FormStock)
        self.lbl_totalAmount.setGeometry(QtCore.QRect(800, 630, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_totalAmount.setFont(font)
        self.lbl_totalAmount.setObjectName("lbl_totalAmount")

        self.retranslateUi(FormStock)
        QtCore.QMetaObject.connectSlotsByName(FormStock)

    def retranslateUi(self, FormStock):
        _translate = QtCore.QCoreApplication.translate
        FormStock.setWindowTitle(_translate("FormStock", "Form"))
        self.table_stock.setSortingEnabled(True)
        self.groupBox.setTitle(_translate("FormStock", "Malzeme Ara"))
        self.lbl_productCode.setText(_translate("FormStock", "Malzeme Kodu :"))
        self.lbl_productName.setText(_translate("FormStock", "Malzeme Adı :"))
        self.lbl_productMainGroup.setText(_translate("FormStock", "Malzeme Üst Grup :"))
        self.lbl_productSecondGroup.setText(_translate("FormStock", "Malzeme Alt Grup :"))
        self.btn_list.setText(_translate("FormStock", "Listele"))
        self.gBox_Filter1.setTitle(_translate("FormStock", "Filtre 1"))
        self.label_9.setText(_translate("FormStock", "Sütun :"))
        self.label_10.setText(_translate("FormStock", "Değer :"))
        self.gBox_Filter2.setTitle(_translate("FormStock", "Filtre 2"))
        self.label_15.setText(_translate("FormStock", "Sütun :"))
        self.label_16.setText(_translate("FormStock", "Değer :"))
        self.gBox_displaySettings.setTitle(_translate("FormStock", "Görüntüleme"))
        self.gBox_stokManageGuide.setTitle(_translate("FormStock", "Kılavuz"))
        self.lbl_filters.setText(_translate("FormStock", "Filtre : Seçilmedi."))
        self.btn_refreshFilters.setText(_translate("FormStock", "Sıfırla"))
        self.lbl_totalRecord.setText(_translate("FormStock", "Toplam Kayıt : "))
        self.lbl_totalAmount.setText(_translate("FormStock", "Toplam Miktar : "))
