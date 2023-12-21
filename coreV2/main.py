import sys
from PyQt5.QtWidgets import QApplication, QTabWidget
from PyQt5 import QtWidgets
from ui.py_files.MainWindow import Ui_MainWindow

from ui.tabs.FormStock import FormStockTab
from ui.tabs.FormProductTypes import FormProductTypeTab
from ui.tabs.FormProductGroups import FormProductGroupTab
from ui.tabs.FormStockAccept import FormStockAcceptTab
from ui.tabs.FormProductFoam import FormProductFoamTab


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Add a tab widget to the main window
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Make the tabs closable
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)

        # Connect the tabCloseRequested signal to the closeTab slot
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.ui.menubar.triggered.connect(self.open_tab)

    def close_tab(self, index):
        """Close the tab at the given index"""
        tab = self.tab_widget.tabText(index)
        self.tab_widget.removeTab(index)

        self.delete_tabObj(tab, "Depo Durumu","FormStock")
        self.delete_tabObj(tab, "Malzeme Cinsleri","FormProductType")
        self.delete_tabObj(tab, "Malzeme Grupları","FormProductGroup")
        self.delete_tabObj(tab, "Depo Giriş","StockAcceptForm")
        self.delete_tabObj(tab, "Sünger Tanımlar","FormProductFoam")
    
    def delete_tabObj (self, current_tab, tab_title, form_objName):

        if current_tab == tab_title :
            self.tab_widget.findChild(QTabWidget,form_objName).deleteLater()
    
    def open_tab(self, obj):
        action = obj.objectName()
      
        if action == "act_inventoryStatus":
            is_tab = self.tab_widget.findChild(QTabWidget,"FormStock")
    
            if is_tab is not None:
                self.tab_widget.setCurrentWidget(is_tab)
            else:
                tab = FormStockTab()
                self.tab_widget.addTab(tab, 'Depo Durumu')

            is_tab = self.tab_widget.findChild(QTabWidget,"FormStock")
            self.tab_widget.setCurrentWidget(is_tab)

        if action == "act_productTypes":
            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductType")

            if is_tab is not None:
                self.tab_widget.setCurrentWidget(is_tab)
            else:
                tab = FormProductTypeTab()
                self.tab_widget.addTab(tab, 'Malzeme Cinsleri')

            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductType")
            self.tab_widget.setCurrentWidget(is_tab)

        if action == "act_productGroup":
            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductGroup")

            if is_tab is not None:
                self.tab_widget.setCurrentWidget(is_tab)
            else:
                tab = FormProductGroupTab()
                self.tab_widget.addTab(tab, 'Malzeme Grupları')

            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductGroup")
            self.tab_widget.setCurrentWidget(is_tab)

        if action == "act_stockAccept":
            is_tab = self.tab_widget.findChild(QTabWidget,"StockAcceptForm")

            if is_tab is not None:
                self.tab_widget.setCurrentWidget(is_tab)
            else:
                tab = FormStockAcceptTab()
                self.tab_widget.addTab(tab, 'Depo Giriş')

            is_tab = self.tab_widget.findChild(QTabWidget,"StockAcceptForm")
            self.tab_widget.setCurrentWidget(is_tab)
        
        if action == "act_foam":
            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductFoam")

            if is_tab is not None:
                self.tab_widget.setCurrentWidget(is_tab)
            else:
                tab = FormProductFoamTab()
                self.tab_widget.addTab(tab, 'Sünger Tanımlar')

            is_tab = self.tab_widget.findChild(QTabWidget,"FormProductFoam")
            self.tab_widget.setCurrentWidget(is_tab)



        if action == "act_dashboard":
            tab = QTabWidget()
            self.tab_widget.addTab(tab, 'Dashboard')
            
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())