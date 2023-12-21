from PyQt5.QtWidgets import QRadioButton,QTableWidgetItem

class TableManager:
    def __init__(self, masterclass, table_obj) -> None:
        
        self.masterClass = masterclass
        self.get_headers()
        self.table = table_obj
        self.set_headers()
    
    def get_headers(self):
        headers = []
        for keyword in self.masterClass.sql_keywords:
            headers.append(keyword[1])
        
        self.headers = headers
    
    def set_radioButtons(self, grid_obj, gbox_obj):
        
        column_index = 0
        row_index = 0

        for header in self.headers:
            if column_index / 3 != 1:
                grid_obj.addWidget(QRadioButton(header),row_index,column_index)
                column_index += 1
            else:
                grid_obj.addWidget(QRadioButton(header),row_index,column_index)
                row_index += 1 
                column_index = 0
        
        self.radio_buttons = gbox_obj.findChildren(QRadioButton)

        for button in self.radio_buttons:
            button.setAutoExclusive(False)
            button.setChecked(True)
            button.clicked.connect(self.tab_event_handler)
          
    def set_headers(self):
    
        labels = []
        for header in self.headers:
            labels.append(header)
        labels = tuple(labels)

        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(labels)

    def tuple_to_dict(self, database):
        dict = {}
        for data in database:
            dict[data[0]] = {}
            n = 1
            for header in self.headers:
                dict[data[0]][header] = data[n]
                n += 1
        return dict
    
    def dictate_data(self, database, keywords):
        # better version of 'tuple_to_dict' function
        dict = {}
        for data in database:
            dict[data[0]] = {}
            tuple_index = 1
            for keyword in keywords:
                dict[data[0]][keyword] = data[tuple_index]
                tuple_index += 1
        
        return dict
    
    def load_table(self, database):
        item_count = len(database)
        self.table.setRowCount(item_count)
        row_index = 0
        for row in database:
            column_index = 0
            for header in self.headers:
                self.table.setItem(row_index,column_index,QTableWidgetItem(str(database[row][header])))
                column_index += 1
            row_index += 1
            
    def tab_event_handler(self, event):
        headercount = self.table.columnCount()
    
        if event:
            for button in self.radio_buttons:
                status = button.isChecked()
                if status:
                    obj_name = button.text()
                    for index in range(headercount):
                        headertext = self.table.horizontalHeaderItem(index).text()
                        if headertext == obj_name:
                            self.table.setColumnHidden(index, False)
                            break
        else:
            for button in self.radio_buttons:
                status = button.isChecked()
                if status == False:
                    obj_name = button.text()
                    for index in range(headercount):
                        headertext = self.table.horizontalHeaderItem(index).text()
                        if headertext == obj_name:
                            self.table.setColumnHidden(index, True)
                            break

    def filter_string_editor(self, filters, label, button):
        for filter in filters:
            text = filter[1]
            if text != "":
                filter[2] = True

        filter_string = ""

        for filter in filters:
            if filter[2]:
                string = filter[0] + "=" + f"'{filter[1]}',"
                filter_string += string

        if filter_string != "":
            label.setText(filter_string)
            button.show()


class CbFilter:
    def __init__(self, masterClass ,column_cb, row_cb, table_obj) :
        
        self.tableManager  = TableManager(masterClass, table_obj)
        self.masterClass = masterClass
        self.column_cb = column_cb
        self.row_cb = row_cb

        column_cb.addItem("")

        headers = []
        for keyword in self.masterClass.sql_keywords:
            headers.append(keyword[1])
        
        self.headers = headers
        for header in self.headers:
            column_cb.addItem(header)

    def set_data(self, database):
        self.database = database

    def load_rowKeys(self,keyword):
        self.row_cb.clear()
        self.row_cb.addItem("")
        
        print(self.database)
        list = []
        
        try:
            for data in self.database:
                item = str(self.database[data][keyword])
                if item not in list:
                    list.append(item)

            if len(list) != 0:
                for item in list:
                    self.row_cb.addItem(item)
        except:
            pass # combobox da boşluk bırakınca 


     
        

