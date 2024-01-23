from tinydb import TinyDB, Query
from tinydb.database import Document


class SmartphoneDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path, indent=4, separators=(',', ': '))
        self.query = Query()
    
    def all_smartphone(self):
        brands_all = ["Huawei","Redmi","Vivo","Nokia","Apple","Oppo","Samsung"]
        smartphones = []
        for brand in brands_all:
            brand_all = self.db.table(brand).all()
            smartphones.append(brand_all)
        return smartphones

    def brands(self):
        """Returns all brands in the database"""
        brand = self.db.tables()
        return list(brand)
    
    def get_smartphone_by_brand(self, brand):
        """Returns all products by brand"""
        data = self.db.table(brand)
        return data.all()
    
    def get_smartphone_by_name(self, name):
        """Returns a product by name"""
        brands_all = ["Huawei","Redmi","Vivo","Nokia","Apple","Oppo","Samsung"]
        smartpone = []
        for brand in brands_all:
            data = self.db.table(brand).search(self.query.name==name)
            if data!=[]:
                smartpone.append(data)
        return smartpone[0]
    
    def get_smartphone_by_price(self, price):
        """Returns a product by price"""
        brands_all = ["Huawei","Redmi","Vivo","Nokia","Apple","Oppo","Samsung"]
        smartpone = []
        for brand in brands_all:
            data = self.db.table(brand).search(self.query.price == price)
            if data != []:
                smartpone.append(data)
        return smartpone
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        phone = self.db.table(brand)
        phone.insert(smartphone)
        return {"statust":"ok"}
    
    def delete_smartphone(self, doc_id, brand):
        """Deletes a product from the database"""
        phone = self.db.table(brand)
        phone.remove(doc_ids=[doc_id])
        return {"statust":"ok"}
    
if __name__=="__main__":
    db = SmartphoneDB('db.json')

    # print(db.all_smartphone())
    # print(db.brands())
    # print(db.get_smartphone_by_brand('Nokia'))
    # print(db.get_smartphone_by_name('Apple iPhone 6s'))
    # print(db.get_smartphone_by_price('Apple', 851.6))
    # smartphone = {
    #         "name":"Apple i13Pro",
    #         "company":"Apple",
    #         "color": "Blue",
    #         "RAM": "8GB",
    #         "memory": "128GB",
    #         "price":13400.3,
    #         "img_url":"https://images-na.ssl-images-amazon.com/images/I/51qBzX0pGYL._SL1000_.jpg"
    #     }
    # print(db.add_smartphone(brand="Apple", smartphone=smartphone))
    # print(db.delete_smartphone(brand="Apple", doc_id=30))