from PyQt5.QtWidgets import QTableWidgetItem



class DataManager:
    def __init__(self, table):

        self.table = table
        self.keywords = []
        self.filters = []

    def set_tuple(self, tuples, keywords):
        dict = {}
        for tuple in tuples:
            dict[tuple[0]] = {}
            tuple_index = 1
            for keyword in keywords:
                self.keywords.append((tuple_index, keyword))
                dict[tuple[0]][keyword] = tuple[tuple_index]
                tuple_index += 1
        
        self.keywords = keywords
        self.database = dict
        print(self.database)

    def insert_keyword(self, keyword, values):
        self.keywords.append((len(self.keywords)+1, keyword))

        index = 0
        for data in self.database:
            self.database[data][keyword] = values[index]
            index  += 1

    def set_filter(self, keyword, value):
        if len(self.filters) != 0:
            for filter in self.filters:
                if filter[0] == keyword:
                    return False
        else:
            self.filters.append([keyword, value])

    def remove_filters(self):
        self.filters = []

    def eliminate_data(self):
        database_copy = self.database.copy()

        if len(self.filters) != 0:
            for data in self.database:
                for filter in self.filters:
                    if self.database[data][filter[0]].startswith(filter[1]):
                        pass
                    else:
                        database_copy.pop(data)
            
            self.database = database_copy
    
    def set_headers(self, keywords):
        labels = []
        for header in keywords:
            labels.append(header)
        labels = tuple(labels)

        self.table.setColumnCount(len(keywords))
        self.table.setHorizontalHeaderLabels(labels)
    
    def load_table(self, keywords):

        self.set_headers(keywords)

        item_count = len(self.database)
        self.table.setRowCount(item_count)
        row_index = 0
        for row in self.database:
            column_index = 0
            for header in keywords:
                self.table.setItem(row_index,column_index,QTableWidgetItem(str(self.database[row][header])))
                column_index += 1
            row_index += 1
    
    def order_dict(self, order_list):
        ordered_dict = {}
        for id in self.database:
            ordered_dict[id] = {}
            dict = self.database[id]
            sorted_keys = sorted(dict.keys(), key=lambda x: order_list.index(x))
            for key in sorted_keys:
                print(key, dict[key])
                ordered_dict[id][key] = dict[key] 
                
        self.database = ordered_dict
        print(self.database)
       