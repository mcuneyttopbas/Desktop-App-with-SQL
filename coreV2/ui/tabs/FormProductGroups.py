from PyQt5.QtWidgets import QTabWidget, QDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5 import QtGui


from ui.py_files.FormProductGroup import Ui_FormProductGroup

from db_manager import DbManager
from table_manager import TableManager
from product import ProductType, MainCategory, SecondaryCategory

db = DbManager()

class FormProductGroupTab(QTabWidget):

    def __init__(self):
        super(FormProductGroupTab, self).__init__()

        self.ui = Ui_FormProductGroup()
        self.ui.setupUi(self)
        self.load_firstTable()

        self.ui.list_main.currentItemChanged.connect(self.load_secondTable)

        self.ui.btn_addMain.clicked.connect(self.add_main)
        self.ui.btn_editMain.clicked.connect(self.edit_main)
        self.ui.btn_deleteMain.clicked.connect(self.delete_main)

        self.ui.btn_addSecond.clicked.connect(self.add_second)
        self.ui.btn_editSecond.clicked.connect(self.edit_second)
        self.ui.btn_deleteSecond.clicked.connect(self.delete_second)

    def feedback_messageBox(self,item,event=""):
            msg = QMessageBox()
            msg.setWindowTitle("İşlem Raporu")
            msg.setText(f"{item} {event}.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon('icon.png'))
            msg.raise_()
            x = msg.exec_()

    def load_firstTable(self):
        self.ui.list_main.clear()
        self.main_database = db.get_all_data(MainCategory)

        for category in self.main_database:
            self.ui.list_main.addItem(str(category[1]))
    
    def load_secondTable(self):
        self.ui.list_second.clear()
        self.second_database = db.get_all_data(SecondaryCategory)
        try:
            self.index = self.ui.list_main.currentRow()
            self.item = self.ui.list_main.item(self.index).text()

            tuple = [tup for tup in self.main_database if self.item in tup]
            self.mainCategory_id = tuple[0][0]

            for category in self.second_database:
                if category[2] == self.mainCategory_id:
                    self.ui.list_second.addItem(category[1])
        except:
            pass

    def add_main(self):
        while True:
            text, ok = QInputDialog.getText(self, "Üst Grup Ekle", "Üst Grup belirle:")
            if ok and text is not None and text.isspace()== False:
                obj = MainCategory(0,text)
                db.add_data(obj)
                self.load_firstTable()
                break
            elif not ok:
                break
            else:
                self.feedback_messageBox("Lütfen kutucuğu boş bırakmayınız.")

    def edit_main(self):
        try:
            main_index = self.ui.list_main.currentRow()
            main_item = self.ui.list_main.item(main_index).text()
        
            mainCategory_id = db.get_data("main_categories","mainCategory_name", main_item)[0]

            while True:
                text, ok = QInputDialog.getText(self, "Üst Grup Düzenle", f"{self.item} düzenle:", QLineEdit.Normal, main_item)
                if ok and text is not None and text.isspace()== False:
                    obj = MainCategory(mainCategory_id, text)
                    db.edit_data("mainCategory_id" ,mainCategory_id, obj)
                    self.feedback_messageBox(main_item, f"{text} olarak düzenlendi")
                    self.load_firstTable()
                    break
                elif not ok:
                    break
                else:
                    self.feedback_messageBox("Lütfen kutucuğu boş bırakmayınız.")
        except AttributeError:
            self.feedback_messageBox("Lütfen Seçim Yapınız")

    def delete_main(self):
        try:
            main_index = self.ui.list_main.currentRow()
            main_item = self.ui.list_main.item(main_index).text()
            mainCategory_id = db.get_data("main_categories","mainCategory_name", main_item)[0]

            if db.check_foreign_byID(mainCategory_id, "secondary_categories", "secondaryCategory_mainCategory_id"):
                raise Exception

            q = QMessageBox.question(self, "Üst Grup Sil", "Üst Grup'u silmek istiyor musunuz? : " + main_item, QMessageBox.Yes | QMessageBox.No)
            if q == QMessageBox.Yes:
                db.delete_data("main_categories","mainCategory_id", mainCategory_id)
                self.load_firstTable() 
                self.feedback_messageBox(main_item, "veritabanından silindi")
        except AttributeError:
            self.feedback_messageBox("Lütfen Seçim Yapınız")
        except Exception:
            self.feedback_messageBox("Silmek istediğiniz kayıt diğer kayıtlarda kullanılmaktadır")

    def add_second(self):
        while True:
            text, ok = QInputDialog.getText(self, "Alt Grup Ekle", f"{self.item}'a bağlı bir Alt Grup belirle:")
            if ok and text is not None and text.isspace()== False:
                print(f"id: {self.mainCategory_id}")
                obj = SecondaryCategory(0, text, self.mainCategory_id)
                db.add_data(obj)
                self.feedback_messageBox(text, "veritabanına eklendi")
                self.load_firstTable() 
                break
            elif not ok:
                break
            else:
              self.feedback_messageBox("Lütfen kutucuğu boş bırakmayınız.")  

    def edit_second(self):
        try:
            main_index = self.ui.list_main.currentRow()
            main_item = self.ui.list_main.item(main_index).text()
            mainCategory_id = db.get_data("main_categories","mainCategory_name", main_item)[0]

            second_index = self.ui.list_second.currentRow()
            second_item = self.ui.list_second.item(second_index).text()
            secondCategory_id = db.get_data("secondary_categories","secondaryCategory_name", second_item)[0]
        
            while True:
                text, ok = QInputDialog.getText(self, "Alt Grup Düzenle", f"{main_item}>{second_item} düzenle:", QLineEdit.Normal, second_item)
                if ok and text is not None and text.isspace()== False:
                    obj = SecondaryCategory(secondCategory_id,text,mainCategory_id)
                    db.edit_data("secondaryCategory_id" ,secondCategory_id, obj)
                    self.feedback_messageBox(second_item, f"{text} olarak düzenlendi")
                    self.load_firstTable()
                    break
                elif not ok:
                    break
                else:
                    self.feedback_messageBox("Lütfen kutucuğu boş bırakmayınız.")
        except AttributeError:
            self.feedback_messageBox("Lütfen seçim yapınız")


    def delete_second(self):
        try:
            second_index = self.ui.list_second.currentRow()
            second_item = self.ui.list_second.item(second_index).text()
            secondCategory_id = db.get_data("secondary_categories","secondaryCategory_name", second_item)[0]

            if db.check_foreign_byID(secondCategory_id, "product_types", "productType_secondaryCategory_id"):
                raise Exception

            q = QMessageBox.question(self, "Üst Grup Sil", "Üst Grup'u silmek isteiyor musunuz? : " + second_item, QMessageBox.Yes | QMessageBox.No)
            if q == QMessageBox.Yes:
                db.delete_data("secondary_categories","secondaryCategory_id", secondCategory_id)
                self.load_firstTable() 
                self.feedback_messageBox(second_item, "veritabanından silindi")
        except AttributeError:
            self.feedback_messageBox("Lütfen Seçim Yapınız")
        except Exception:
            self.feedback_messageBox("Silmek istediğiniz kayıt diğer kayıtlarda kullanılmaktadır")



