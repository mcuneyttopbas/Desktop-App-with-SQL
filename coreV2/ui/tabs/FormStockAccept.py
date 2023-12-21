from PyQt5.QtWidgets import QTabWidget


from ui.py_files.FormStockAccept import Ui_StockAcceptForm

from product import MainCategory

from db_manager import DbManager

db = DbManager()


class FormStockAcceptTab(QTabWidget):

    def __init__(self):
        super(FormStockAcceptTab, self).__init__()

        self.ui = Ui_StockAcceptForm()
        self.ui.setupUi(self)

        self.load_categoryCb()

        self.ui.cb_mainCategory.currentTextChanged.connect(self.load_table)

    def load_categoryCb(self):
        self.categories = db.get_all_data(MainCategory)
        self.ui.cb_mainCategory.addItem("")
        for category in self.categories:
            self.ui.cb_mainCategory.addItem(category[1])
    
    def load_table(self, category):
        pass