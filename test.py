import pickle

with open('products.pkl', 'rb') as f:
    product_list = pickle.load(f)

count = 0
category = 'camera'

for product in product_list:
    if product_list[product].category == category:
        print(product_list[product].name)
        count += 1
    if count > 20:
        break