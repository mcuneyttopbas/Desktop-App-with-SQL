from db_connection import connection

cursor = connection.cursor()


query = ("""CREATE TABLE IF NOT EXISTS main_categories
            (mainCategory_id INTEGER PRIMARY KEY,
            mainCategory_name TEXT NOT NULL
            );""")     
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS secondary_categories
            (secondaryCategory_id INTEGER PRIMARY KEY,
            secondaryCategory_name TEXT NOT NULL,
            secondaryCategory_mainCategory_id INTEGER NOT NULL,
            FOREIGN KEY(secondaryCategory_mainCategory_id) REFERENCES main_categories(mainCategory_id)
            );""")           
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS product_types
            (productType_id INTEGER PRIMARY KEY,
            productType_name TEXT NOT NULL,
            productType_status TEXT NOT NULL,
            productType_mainCategory_id INTEGER NOT NULL,
            productType_secondaryCategory_id INTEGER NOT NULL,
            FOREIGN KEY(productType_mainCategory_id) REFERENCES main_categories(mainCategory_id)
            FOREIGN KEY(productType_secondaryCategory_id) REFERENCES secondary_categories(secondaryCategory_id)
            );""")
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS products
            (product_id INTEGER PRIMARY KEY,
            product_productType_id TEXT NOT NULL,
            product_code TEXT NOT NULL,
            product_unit TEXT NOT NULL,
            product_totalAmount INTEGER NULL,
            product_unreservedAmount INTEGER,
            FOREIGN KEY(product_productType_id) REFERENCES product_types(productType_id)
            );""")
connection.execute(query)


query = ("""CREATE TABLE IF NOT EXISTS foam_details
            (foam_id INTEGER PRIMARY KEY,
            foam_color TEXT NOT NULL,
            foam_density INTEGER NOT NULL,
            foam_thickness INTEGER NOT NULL,
            foam_width INTEGER NOT NULL,
            foam_product_id INTEGER NOT NULL,
            FOREIGN KEY(foam_product_id) REFERENCES products(product_id)
            );""")
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS suppliers
            (supplier_id INTEGER PRIMARY KEY,
            supplier_brandName TEXT NOT NULL,
            supplier_officialName TEXT NOT NULL,
            supplier_adress TEXT NOT NULL,
            supplier_area TEXT NOT NULL,
            supplier_city TEXT NOT NULL,
            supplier_country TEXT NOT NULL,
            supplier_zipCode TEXT NOT NULL,
            supplier_phone1 TEXT NOT NULL,
            supplier_phone TEXT NOT NULL,
            supplier_fax TEXT NOT NULL,
            supplier_responsible TEXT NOT NULL,
            supplier_responsiblePhone TEXT NOT NULL,
            supplier_responsibleEmail TEXT NOT NULL,
            supplier_notes TEXT NOT NULL,
            supplier_taxAuthority TEXT NOT NULL,
            supplier_taxCode TEXT NOT NULL
            );""")
connection.execute(query)


query = ("""CREATE TABLE IF NOT EXISTS lot_details
            (lot_id INTEGER PRIMARY KEY,
            lot_supplier_id TEXT NOT NULL,
            lot_product_id INTEGER NOT NULL,
            lot_code INTEGER NOT NULL,
            lot_price INTEGER NOT NULL,
            lot_date INTEGER NOT NULL,
            lot_deliveryDocumentNo TEXT,
            lot_totalAmount INTEGER NOT NULL,
            FOREIGN KEY(lot_product_id) REFERENCES products(product_id)
            FOREIGN KEY(lot_supplier_id) REFERENCES suppliers(supplier_id)
            );""")
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS transfer_receipts
            (transferReceipt_id INTEGER PRIMARY KEY,
            transferReceipt_code INTEGER NOT NULL,
            transferReceipt_direction TEXT NOT NULL,
            transferReceipt_type TEXT NOT NULL,
            transferReceipt_date TEXT NOT NULL,
            transferReceipt_description TEXT NOT NULL
            );""")
connection.execute(query)

query = ("""CREATE TABLE IF NOT EXISTS transfer_contents
            (transferContent_id INTEGER PRIMARY KEY,
            transferContent_transferReceipt_id INTEGER NOT NULL,
            transferContent_product_id INTEGER NOT NULL,
            FOREIGN KEY(transferContent_transferReceipt_id) REFERENCES transfer_receipts(transferReceipt_id)
            FOREIGN KEY(transferContent_product_id) REFERENCES products(product_id)
            );""")
connection.execute(query)

