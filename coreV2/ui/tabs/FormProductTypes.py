from PyQt5.QtWidgets import QTabWidget, QDialog, QMessageBox
from PyQt5 import QtGui

from ui.py_files.FormProductType import Ui_FormProductType
from ui.py_files.DialogProductType import Ui_DialogProductType

from db_manager import DbManager
from table_manager import TableManager
from product import ProductType, MainCategory, SecondaryCategory

db = DbManager()

class FormProductTypeTab(QTabWidget):

    def __init__(self):
        super(FormProductTypeTab, self).__init__()

        self.ui = Ui_FormProductType()
        self.ui.setupUi(self)
        self.additional_uiSetup()

        self.tableManager = TableManager(ProductType, self.ui.table_productTypes)

        self.get_data()

        self.ui.btn_list.clicked.connect(self.search_product)
        self.ui.btn_refreshFilters.clicked.connect(self.refresh_filters)
        self.ui.btn_refresh.clicked.connect(self.refresh_filters)
        self.ui.cb_mainCat.currentTextChanged.connect(self.load_secondaryCategories)

        self.ui.btn_add.clicked.connect(self.add_productType)
        self.ui.btn_edit.clicked.connect(self.edit_productType)
        self.ui.btn_delete.clicked.connect(self.delete_productType)

    def feedback_messageBox(self,item,event=""):
            msg = QMessageBox()
            msg.setWindowTitle("İşlem Raporu")
            msg.setText(f"{item} {event}.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon('icon.png'))
            msg.raise_()
            x = msg.exec_()
    
    def keep_record(self):
        count = str(len(self.productTypes_data))
        self.ui.lbl_records.setText(count)

    def get_data(self):
        productTypes_list = db.get_productTypes_data()
        self.productTypes_data = self.tableManager.tuple_to_dict(productTypes_list)
        self.tableManager.load_table(self.productTypes_data)
        self.load_mainCategories()
        self.keep_record()

    def additional_uiSetup(self):
        self.ui.cb_status.addItem("")
        self.ui.cb_status.addItem("Aktif")
        self.ui.cb_status.addItem("Pasif")
        self.ui.cb_status.addItem("Kullanım Dışı")
    
    def search_product(self):
        updated_data = self.productTypes_data.copy()

        productType_name = self.ui.txt_productType.text()
        productType_mainCategory = self.ui.cb_mainCat.currentText()
        productType_secondaryCategory = self.ui.cb_secondaryCat.currentText()
        productType_status = self.ui.cb_status.currentText()

        filters = [
            ["Malzeme Cins",productType_name , False, "btn"],
            ["Üst Grup", productType_mainCategory, False, "btn"],
            ["Alt Grup", productType_secondaryCategory, False,"btn" ],
            ["Durum", productType_status,False, "btn"]]

        self.tableManager.filter_string_editor(filters, self.ui.lbl_filters, self.ui.btn_refreshFilters)

        for product in self.productTypes_data:
            if self.productTypes_data[product]["Malzeme Cinsi"].startswith(productType_name):
                if self.productTypes_data[product]["Üst Grup"].startswith(productType_mainCategory):
                    if self.productTypes_data[product]["Alt Grup"].startswith(productType_secondaryCategory):
                        if self.productTypes_data[product]["Durum"].startswith(productType_status):
                            continue
                        else:
                            updated_data.pop(product)
                    else:        
                        updated_data.pop(product)
                else:
                    updated_data.pop(product)
            else:
                updated_data.pop(product)
        
        self.productTypes_data = updated_data
        self.tableManager.load_table(self.productTypes_data)

    def refresh_filters(self):
        self.ui.txt_productType.clear()
        self.ui.cb_mainCat.setCurrentText("")
        self.ui.cb_secondaryCat.setCurrentText("")
        self.ui.cb_status.setCurrentText("")
        self.ui.lbl_filters.setText("Filtre Seçilmedi")

        self.get_data()

    def load_mainCategories(self):

        list = []

        try:
            for data in self.productTypes_data:
                item = str(self.productTypes_data[data]["Üst Grup"])
                if item not in list:
                    list.append(item)
        
            if len(list) != 0:
                self.ui.cb_mainCat.clear()
                self.ui.cb_mainCat.addItem("")
                for item in list:
                    self.ui.cb_mainCat.addItem(item)
        except:
            print("hata versdi")

    def load_secondaryCategories(self, keyword):
        list = []

        try:
            for data in self.productTypes_data:
                mainCategory = str(self.productTypes_data[data]["Üst Grup"])
                if mainCategory == keyword:
                    secondaryCategory = self.productTypes_data[data]["Alt Grup"]
                    if secondaryCategory not in list:
                        list.append(secondaryCategory)

            if len(list) != 0:
                self.ui.cb_secondaryCat.clear()
                self.ui.cb_secondaryCat.addItem("")
                for item in list:
                    self.ui.cb_secondaryCat.addItem(item)

        except Exception as err:
            print(f"error : {err}")


    def edit_productType(self):
        try:
            self.dialog = DialogProductType("Malzeme Cins Düzenle")
            mainCategories = db.get_all_data(MainCategory)
            secondaryCategories = db.get_all_data(SecondaryCategory)
            
            def load_secondaryCategories(keyword):
            
                self.dialog.ui.cb_secondCat.clear()
                tuple = [tup for tup in mainCategories if keyword in tup]
                category_id = tuple[0][0]
            
                self.dialog.ui.cb_secondCat.addItem("")
                for category in secondaryCategories:
                    if category[2] == category_id:
                        self.dialog.ui.cb_secondCat.addItem(category[1])

            self.ui.cb_mainCat.addItem("")
            for category in mainCategories:
                self.dialog.ui.cb_mainCat.addItem(category[1])

            self.dialog.ui.cb_status.addItem("Aktif")
            self.dialog.ui.cb_status.addItem("Pasif")
            self.dialog.ui.cb_status.addItem("Kullanım Dışı")
            
  
            current_row = self.ui.table_productTypes.currentRow()
            self.productType_mainCategory = self.ui.table_productTypes.item(current_row, 1).text()
            self.productType_secondaryCategory = self.ui.table_productTypes.item(current_row, 2).text()
            self.productType_status = self.ui.table_productTypes.item(current_row, 0).text()
            self.productType_name = self.ui.table_productTypes.item(current_row, 3).text()

            productType_id = db.get_productType(self.productType_name)[0]

            index1 = self.dialog.ui.cb_mainCat.findText(self.productType_mainCategory)
            index2 = self.dialog.ui.cb_secondCat.findText(self.productType_secondaryCategory)
            index3 = self.dialog.ui.cb_status.findText(self.productType_status)
    
            self.dialog.ui.cb_mainCat.setCurrentIndex(index1)
            self.dialog.ui.cb_secondCat.setCurrentIndex(index2)
            self.dialog.ui.cb_status.setCurrentIndex(index3)
            self.dialog.ui.txt_productType.setText(self.productType_name)

            tuple = [tup for tup in mainCategories if self.dialog.ui.cb_mainCat.currentText() in tup]
            category_id = tuple[0][0]
        
            for category in secondaryCategories:
                if category[2] == category_id:
                    self.dialog.ui.cb_secondCat.addItem(category[1])
                    
        
            def save_data():
                self.productType_mainCategory = self.dialog.ui.cb_mainCat.currentText()
                self.productType_secondaryCategory = self.dialog.ui.cb_secondCat.currentText()
                self.productType_status = self.dialog.ui.cb_status.currentText()
                self.productType_name = self.dialog.ui.txt_productType.text()
                try:
                    list = [self.productType_mainCategory, self.productType_secondaryCategory,self.productType_status,self.productType_name ]
                    for item in list:
                        if item == "" or item == None:
                            raise Exception 
                    tuple = [tup for tup in mainCategories if self.productType_mainCategory in tup]
                    self.productType_mainCategory = tuple[0][0]
                    tuple = [tup for tup in secondaryCategories if self.productType_secondaryCategory in tup]
                    self.productType_secondaryCategory = tuple[0][0]

                    db.edit_productType(productType_id,self.productType_name, self.productType_mainCategory,self.productType_secondaryCategory,self.productType_status)
                    self.feedback_messageBox(self.productType_name, "başarıyla düzenlendi")
                    self.dialog.close()
                    self.refresh_filters()
                except Exception as err:
                    self.feedback_messageBox(f"Lütfen boşluk bırakmayınız! {err}")
                    

            self.dialog.ui.cb_mainCat.currentTextChanged.connect(load_secondaryCategories)
            self.dialog.ui.btn_save.clicked.connect(save_data)
            self.dialog.setModal(True)
            self.dialog.exec()
        except AttributeError:
            self.feedback_messageBox("Lütfen seçim yapınız")
            
    
    def add_productType(self):
        self.dialog = DialogProductType("Malzeme Ekle")
        mainCategories = db.get_all_data(MainCategory)
        secondaryCategories = db.get_all_data(SecondaryCategory)
        
        def load_mainCategories():
            self.dialog.ui.cb_mainCat.addItem("")
            for category in mainCategories:
                self.dialog.ui.cb_mainCat.addItem(category[1])
        
        def setupUi():
            load_mainCategories()
            self.dialog.ui.cb_status.addItem("")
            self.dialog.ui.cb_status.addItem("Aktif")
            self.dialog.ui.cb_status.addItem("Pasif")
            self.dialog.ui.cb_status.addItem("Kullanım Dışı")
        
        def load_secondaryCategories(keyword):
            self.dialog.ui.cb_secondCat.clear()
            tuple = [tup for tup in mainCategories if keyword in tup]
            category_id = tuple[0][0]
            
            self.dialog.ui.cb_secondCat.addItem("")
            for category in secondaryCategories:
                if category[2] == category_id:
                    self.dialog.ui.cb_secondCat.addItem(category[1])
        
        def save_data():

            productType_mainCategory = self.dialog.ui.cb_mainCat.currentText()
            productType_secondaryCategory = self.dialog.ui.cb_secondCat.currentText()
            productType_status = self.dialog.ui.cb_status.currentText()
            productType_name = self.dialog.ui.txt_productType.text()

            try:
                if productType_mainCategory != "":
                    tuple = [tup for tup in mainCategories if productType_mainCategory in tup]
                    productType_mainCategory = tuple[0][0]
                    if productType_secondaryCategory != "":
                        tuple = [tup for tup in secondaryCategories if productType_secondaryCategory in tup]
                        productType_secondaryCategory = tuple[0][0]
                        if productType_status != "":
                            if productType_name != "":
                                obj = ProductType(productType_status, productType_mainCategory, productType_secondaryCategory, productType_name)
                                db.add_data(obj)
                                self.feedback_messageBox(productType_name, "başarıyla kaydedildi")
                                self.refresh_filters()
                self.dialog.close()
            except Exception as err:
                self.feedback_messageBox(err)
        
        setupUi()
        self.dialog.ui.cb_mainCat.currentTextChanged.connect(load_secondaryCategories)
        self.dialog.ui.btn_save.clicked.connect(save_data)
        self.dialog.setModal(True)
        self.dialog.exec()

    def delete_productType(self):
        try:
            current_row = self.ui.table_productTypes.currentRow()
            self.productType_name = self.ui.table_productTypes.item(current_row, 3).text()
            productType_id = db.get_data("product_types","productType_name", self.productType_name)[0]

            if db.check_foreign_byID(productType_id, "products", "product_productType_id"):
                raise Exception

            result = QMessageBox.question(self, 'Malzeme Cins Sil', f'{self.productType_name} veritabanından kalıcı olarak silinecek. Devam etmek istiyor musunuz ?', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if result == QMessageBox.Ok:
                db.delete_data("product_types", "productType_name", self.productType_name)
                self.refresh_filters()
                self.feedback_messageBox(self.productType_name, "silindi")
        except AttributeError:
            self.feedback_messageBox("Lütfen seçim yapınız")
        except Exception:
            self.feedback_messageBox("Silmek istediğiniz kayıt diğer kayıtlarda kullanılmaktadır")


class DialogProductType(QDialog):

    def __init__(self, purpose):
            super(DialogProductType, self).__init__()

            self.ui = Ui_DialogProductType()
            self.ui.setupUi(self)

            self.purpose = purpose
            self.setWindowTitle(purpose)

