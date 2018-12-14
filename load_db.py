import pymongo
from pymongo import MongoClient
import pickle

# mongodb://<dbuser>:<dbpassword>@ds147890.mlab.com:47890/iot-products
# initialize db connection

DB_NAME = 'iot-products'  
DB_HOST = 'ds147890.mlab.com'
DB_PORT = 47890
DB_USER = 'rmohan'
DB_PASS = 'rmohan93'

connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)
collection = db.products

# Load file containing dictionary of products
with open('./scrapes/products_11242018_cleaned.pkl', 'rb') as f:
    product_list = pickle.load(f)

# Convert each entry to JSON object
for product_id in product_list:
    if type(product_list[product_id].price) == float:
        product_obj = {}
        product_obj['_id'] = product_id
        product_obj['name'] = product_list[product_id].name
        product_obj['price'] = product_list[product_id].price
        product_obj['seller'] = product_list[product_id].seller
        product_obj['rating'] = product_list[product_id].rating
        product_obj['desc'] = product_list[product_id].desc
        product_obj['image'] = product_list[product_id].image
        product_obj['assistant'] = product_list[product_id].assistant
        product_obj['category'] = product_list[product_id].category
        product_obj['url'] = product_list[product_id].url
        
        # insert into db
        collection.insert_one(product_obj)
 


    

