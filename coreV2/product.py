class Product:
    table_name = "products"
    sql_keywords = [
        ("code","Malzeme Kodu"),
        ("unit","Birim"),
        ("total_amount", "Toplam Miktar"),
        ("unreserved_amount","Kalan Depo"),
        ("main_category", "Üst Grup"),
        ("secondary_category", "Alt Grup"),
        ("type","Malzeme Cins")]


    def __init__(self, 
                id,
                type,
                code,
                name,
                unit,
                unreserved_amount,
                total_amount):
        
        self.id = id
        self.type = type
        self.code = code
        self.name = name

        self.unit = unit
        self.unreserved_amount = unreserved_amount
        self.total_amount = total_amount

class MainCategory:
    table_name = "main_categories"
    sql_keywords = [("mainCategory_name","Üst Grup")]

    def __init__(self,id, name):

        self.mainCategory_id = id
        self.mainCategory_name = name

class SecondaryCategory:
    table_name = "secondary_categories"
    sql_keywords = [("secondaryCategory_name", "Alt Grup" ),("secondaryCategory_mainCategory_id", "Üst Grup ID")]

    def __init__(self, id, name, main_category_id):
        
        self.secondaryCategory_id = id
        self.secondaryCategory_name = name
        self.secondaryCategory_mainCategory_id = main_category_id

class ProductType:
    table_name = "product_types"
    sql_keywords = [
        ("productType_status","Durum"),
        ("productType_mainCategory_id","Üst Grup"),
        ("productType_secondaryCategory_id","Alt Grup"),
        ("productType_name","Malzeme Cinsi"),
    ]

    def __init__(self, product_type_status, main_category_id, secondary_category_id, product_type_name) -> None:

        self.productType_name = product_type_name
        self.productType_mainCategory_id = main_category_id
        self.productType_secondaryCategory_id = secondary_category_id
        self.productType_status = product_type_status
        

