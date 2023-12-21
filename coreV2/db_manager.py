from db_connection import connection

class DbManager:
    def __init__(self) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def check_foreign_byID(self, upper_id, lower_table, foreignKey):
        try:
            self.cursor.execute(f"SELECT * from {lower_table} WHERE {foreignKey}={upper_id}; ")
            data = self.cursor.fetchall()
            print(data)
            if len(data) != 0:
                return True
            else:
                return False
        except Exception as error:
            print(f"Error: {error}") 
    
    def sql_string_editor(self, sql_keywords):
        
        placeholders = "("
        values = "("
        for parameter in sql_keywords:
            values += parameter[0] + ","
            placeholders += "?,"
        values = values[:-1] + ")"
        placeholders = placeholders[:-1] + ")"

        print(placeholders)
        return values, placeholders

    def add_data(self, obj):
        table = obj.table_name

        values, placeholders = self.sql_string_editor(obj.sql_keywords)
        print(values)
        sql = f"INSERT INTO {table}{values} VALUES {placeholders}"
        data = []
        for value in obj.sql_keywords:
            data.append(getattr(obj, value[0]))
        value = tuple(data)

        try:
            self.cursor.execute(sql,value)
            self.connection.commit()
            print("Data has been successfully inserted.")
        except Exception as error:
            print(f"Error: {error}")

    def edit_data(self, id_keyword, id_value ,obj):
        table = obj.table_name
        
        edited_values  = ""
        for value in obj.sql_keywords:
            try:
                int(getattr(obj, value))
                edited_values += f"{value[0]}={getattr(obj, value[0])}, "
            except:
                edited_values += f"{value[0]}='{getattr(obj, value[0])}', "
        
        edited_values = edited_values[:len(edited_values)-1]
        print(edited_values)
        print("-----")
        print(edited_values[:-1])

        try:
            self.cursor.execute(f"UPDATE {table} SET {edited_values[:-1]} WHERE {id_keyword}={id_value};")
            self.connection.commit()
            print("Data has been successfully edited.")
        except Exception as error:
            print(f"Error: {error}")

    def delete_data(self, table, parameter, value):

        try:
            self.cursor.execute(f"DELETE FROM {table} WHERE {parameter}='{value}'; ")
            self.connection.commit()
            print("Data has been successfully deleted.")
        except Exception as error:
            print(f"Error: {error}")            
    
    def get_data(self, table, parameter, value):
        try:
            self.cursor.execute(f"SELECT * from {table} WHERE {parameter}='{value}'; ")
            data = self.cursor.fetchone()
            return data
        except Exception as error:
            print(f"Error: {error}") 
    
    def get_all_data(self, class_name):
        table = class_name.table_name
        try:
            self.cursor.execute(f"SELECT * from {table}")
            data = self.cursor.fetchall()
            return data
        except Exception as error:
            print(f"Error: {error}") 

    def get_productTypes_data(self):
        sql = '''SELECT productType_id,productType_status,mainCategory_name, secondaryCategory_name,productType_name
                FROM product_types
                INNER JOIN main_categories
                ON product_types.productType_mainCategory_id = main_categories.mainCategory_id
                INNER JOIN secondary_categories
                ON product_types.productType_secondaryCategory_id = secondary_categories.secondaryCategory_id;
              '''
        try:
            # Executing the query
            self.cursor.execute(sql)
            # Fetching rows from the result table
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error: {error}") 

    def get_product_data(self):
        sql = '''SELECT 
                product_id,product_code, 
                product_unit, product_totalAmount, 
                product_unreservedAmount, mainCategory_name, 
                secondaryCategory_name, productType_name
                FROM products
                INNER JOIN product_types
                ON products.product_productType_id = product_types.productType_id
                INNER JOIN main_categories
                ON product_types.productType_mainCategory_id = main_categories.mainCategory_id
                INNER JOIN secondary_categories
                ON product_types.productType_secondaryCategory_id = secondary_categories.secondaryCategory_id;
                '''
        try:
            # Executing the query
            self.cursor.execute(sql)
            # Fetching rows from the result table
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error: {error}") 
        
    def get_productType(self, productType_name ):

        sql = f'''SELECT productType_id
                from product_types
                WHERE productType_name = '{productType_name}'
                '''
        try:
            # Executing the query
            self.cursor.execute(sql)
            # Fetching rows from the result table
            result = self.cursor.fetchone()
            return result
        except Exception as error:
            print(f"Error: {error}") 
    
    def edit_productType(self, productType_id, productType_name, mainCategory_name, secondaryCategory_name, productType_status):

        sql = f'''UPDATE product_types SET
                productType_status = '{productType_status}',
                productType_mainCategory_id = '{mainCategory_name}',
                productType_secondaryCategory_id = '{secondaryCategory_name}',
                productType_name= '{productType_name}'
                WHERE productType_id = '{productType_id}'
                '''
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as error:
            print(f"Error: {error}") 
    
    def get_productFoam(self):

        sql = '''SELECT 
                product_id,product_code, 
                product_unit, product_totalAmount, 
                product_unreservedAmount, mainCategory_name, 
                secondaryCategory_name, productType_name,

                foam_color,foam_density,foam_thickness,foam_width
                
                FROM products
                INNER JOIN product_types
                ON products.product_productType_id = product_types.productType_id
                INNER JOIN main_categories
                ON product_types.productType_mainCategory_id = main_categories.mainCategory_id
                INNER JOIN secondary_categories
                ON product_types.productType_secondaryCategory_id = secondary_categories.secondaryCategory_id
                INNER JOIN foam_details
                ON products.product_id = foam_details.foam_product_id;
                '''
        try:
            # Executing the query
            self.cursor.execute(sql)
            # Fetching rows from the result table
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error: {error}") 