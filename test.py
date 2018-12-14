import pickle

with open('./scrapes/products_11242018_cleaned.pkl', 'rb') as f:
    product_list = pickle.load(f)

count = 0
category = 'smart-plug'

print(len(product_list))

for product_id in product_list:
    if product_list[product_id].category == category:
        print(product_list[product_id].name)
        print(product_list[product_id].assistant)
        count += 1
    if count > 20:
        break