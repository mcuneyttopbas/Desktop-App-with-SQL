from product import Product, MainCategory, SecondaryCategory
from db_manager import DbManager

# product1 = Product(0,"521551","REACT5-X",2,2,"kg",102,350 )
# cat1 = MainCategory(0,"Membran")
# cat2 = SecondaryCategory(0, "Şeffaf", 3)

db = DbManager()
# db.add_data(product1)

# data = db.get_data_by_id("products",1)
# print(data)
# # print(type(data))


# db.check_foreign_byID(4, "product_types", "productType_secondaryCategory_id")

# RESULT = db.get_product_data()

# # print(RESULT)

# list = ["j","oı","k"]
# print(len(list))

# filters = [
#             ["Malzeme Kodu", False, "btn"],
#             ["Malzeme Adı", False, "btn"],
#             ["Üst Grupext()", False,"btn" ],
#             ["Alt Grup",False, "btn"]]

# for filter in filters:
#     if "Mazeme Kodu" in filter:
#         print("yess")

# string="sfksfl"

# t = string.startswith("")

# print(t)

keywords = [
    (4,"Malzeme Kodu"),
    (5,"Birim"),
    (6,"Toplam Miktar"),
    (7,"Kalan Depo"),
    (1,"Üst Grup"),
    (2,"Alt Grup"),
    (3,"Malzeme Cins")
    ]

dict = {'Malzeme Kodu': 'PS B300 ', 'Birim': 'KG', 'Toplam Miktar': 500, 'Kalan Depo': 5, 'Üst Grup': 'Sünger', 'Alt Grup': 'Polyester FR', 
'Malzeme Cins': '2sdfsdfAN'}



# key_index = 1
# for key in keywords:
#     print(f"key is {key}")
#     if key[0] == key_index:
#         print(dict[key[1]])
#         key_index += 1

# value_count = 0
# while value_count != len(keywords):
#     key_index = 1
#     for key in keywords:
#         print(f"key is {key}")
#         if key[0] == key_index:
#             print(dict[key[1]])
#             key_index += 1
#             value_count += 1


result = db.get_product_data()

list = [
    "Üst Grup",
    "Alt Grup",
    "Malzeme Cins"
    "Malzeme Kodu",
    "Birim",
    "Toplam Miktar",
    "Kalan Depo",
]

tuple_reference = {
    "id":0,
    "Malzeme Kodu":1,
    "Birim":2,
    "Toplam Miktar":3,
    "Kalan Depo":4,
    "Üst Grup":5,
    "Alt Grup":6,
    "Malzeme Cins":7
}

my_dict = {'a': 1, 'c': 3, 'b': 2}
custom_order = ['b', 'a', 'c']

sorted_keys = sorted(my_dict.keys(), key=lambda x: custom_order.index(x))

for key in sorted_keys:
    print(key, my_dict[key])

print("deneme")