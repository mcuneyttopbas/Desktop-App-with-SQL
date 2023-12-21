from PyQt5.QtWidgets import QTabWidget

from ui.py_files.FormProductFoam import Ui_FormProductFoam

from db_manager import DbManager
from table_manager import TableManager
from data_manager import DataManager

db = DbManager()

class FormProductFoamTab(QTabWidget):

    def __init__(self, ):
        super(FormProductFoamTab, self).__init__()

        self.ui = Ui_FormProductFoam()
        self.ui.setupUi(self)

        self.ui.btn_list.clicked.connect(self.filter)


        self.keywords = [
            "Malzeme Kodu",
            "Birim",
            "Toplam Miktar",
            "Kalan Depo",
            "Üst Grup",
            "Alt Grup",
            "Malzeme Cins",
            "Renk Adı",
            "Yoğunluk",
            "Kalınlık (mm)",
            "En (cm)"
            ]

        db_data = db.get_productFoam()
        self.data_manager = DataManager(self.ui.table_productFoam)
        self.data_manager.set_tuple(db_data, self.keywords)
        self.data_manager.order_dict(self.keywords)
        self.data_manager.load_table(self.keywords)

    def filter(self):
        
    

        second_cat = self.ui.cb_secondCat.currentText()
        product_code = self.ui.txt_productCode.text()
        product_type = self.ui.txt_productType.text()


        print(second_cat)
        print(product_code)
        print(product_type)

        if second_cat != "":
            self.data_manager.set_filter("Alt Grup",second_cat)
        if product_code != "":
            self.data_manager.set_filter("Malzeme Kodu", product_code)
        if product_type != "":
            self.data_manager.set_filter("Malzeme Cins", product_type)

        print(self.data_manager.filters)
