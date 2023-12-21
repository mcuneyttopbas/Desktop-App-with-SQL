from PyQt5.QtWidgets import QTabWidget, QLineEdit

from ui.py_files.FormStock import Ui_FormStock

from db_manager import DbManager
from table_manager import TableManager, CbFilter
from product import Product

db = DbManager()

class FormStockTab(QTabWidget):

    def __init__(self):
        super(FormStockTab, self).__init__()
    
        self.ui = Ui_FormStock()
        self.ui.setupUi(self)

        self.tableManager = TableManager(Product, self.ui.table_stock)

        self.ui.cb_columnFilter2.setDisabled(True)
        self.ui.cb_rowFilter2.setDisabled(True)
        self.ui.lbl_productName.setText("Malzeme Cinsi :")

        self.tableManager.set_radioButtons(self.ui.gridLayout_displaySettings, self.ui.gBox_displaySettings)

        product_list = db.get_product_data()
        self.product_data = self.tableManager.tuple_to_dict(product_list)
        self.tableManager.load_table(self.product_data)

        self.ui.btn_list.clicked.connect(self.search_product)
        self.ui.btn_refreshFilters.hide()

        self.cb_filter = CbFilter(Product, self.ui.cb_columnFilter1, self.ui.cb_rowFilter1, self.ui.table_stock)
        self.cb_filter.set_data(self.product_data)

        self.ui.cb_columnFilter1.currentTextChanged.connect(self.cb_filter.load_rowKeys)
        self.ui.cb_rowFilter1.currentTextChanged.connect(self.filter_by_combobox)

        self.ui.btn_refreshFilters.clicked.connect(self.refresh_filters)

        self.filters = [
            ["Malzeme Kodu", self.ui.txt_productCode.text(), False, "btn"],
            ["Malzeme Adı", self.ui.txt_productName.text(), False, "btn"],
            ["Üst Grup", self.ui.txt_productMainGroup.text(), False,"btn" ],
            ["Alt Grup", self.ui.txt_productSecondGroup.text(),False, "btn"]]

    def get_filters(self):

        filters = [
            ["Malzeme Kodu", self.ui.txt_productCode.text(), False, "btn"],
            ["Malzeme Adı", self.ui.txt_productName.text(), False, "btn"],
            ["Üst Grup", self.ui.txt_productMainGroup.text(), False,"btn" ],
            ["Alt Grup", self.ui.txt_productSecondGroup.text(),False, "btn"]]
        
        return filters

    def search_product(self):
        updated_data = self.product_data.copy()

        product_code = self.ui.txt_productCode.text()
        product_type = self.ui.txt_productName.text()
        product_main_category = self.ui.txt_productMainGroup.text()
        product_secondary_category = self.ui.txt_productSecondGroup.text()

        filters = self.get_filters()
        self.tableManager.filter_string_editor(filters, self.ui.lbl_filters, self.ui.btn_refreshFilters)

        for product in self.product_data:
            if self.product_data[product]["Malzeme Kodu"].startswith(product_code):
                if self.product_data[product]["Malzeme Cins"].startswith(product_type):
                    if self.product_data[product]["Üst Grup"].startswith(product_main_category):
                        if self.product_data[product]["Alt Grup"].startswith(product_secondary_category):
                            continue
                        else:
                            updated_data.pop(product)
                    else:        
                        updated_data.pop(product)
                else:
                    updated_data.pop(product)
            else:
                updated_data.pop(product)
            
        self.product_data = updated_data
        self.tableManager.load_table(self.product_data)
        self.cb_filter.set_data(updated_data)
        self.cb_filter.load_rowKeys(self.ui.cb_columnFilter1)

    def filter_by_combobox(self, value):
        input_count = len(self.product_data)
        keyword = self.ui.cb_columnFilter1.currentText()
        updated_data = self.product_data.copy()
        
        try:
            if value != "":
                for product in self.product_data:
                    if value != self.product_data[product][keyword]:
                        updated_data.pop(product)
        except:
            for product in self.product_data:
                if value != product:
                    updated_data.pop(product)
      
        self.product_data = updated_data
        self.tableManager.load_table(self.product_data)
        self.cb_filter.set_data(updated_data)

        if input_count != len(updated_data):
            self.cb_filter.load_rowKeys(keyword)
            self.ui.cb_rowFilter1.setCurrentText(value)

            index = 0
            for filter in self.filters:
                if filter[0] == keyword:
                    self.filters[index][1] = value

                index += 1

            self.tableManager.filter_string_editor(self.filters, self.ui.lbl_filters, self.ui.btn_refreshFilters)
    
    def refresh_filters(self):
        product_list = db.get_product_data()
        self.product_data = self.tableManager.tuple_to_dict(product_list)
        self.tableManager.load_table(self.product_data)
        self.ui.lbl_filters.setText("")
        lineEdits = self.ui.groupBox.findChildren(QLineEdit)
        for lineEdit in lineEdits:
            lineEdit.setText("")
        self.ui.cb_columnFilter1.setCurrentIndex(0)
        self.ui.cb_rowFilter1.setCurrentIndex(0)











        