import pickle
from amazon_scraper import AmazonScraper

def find_assistant(product):
    assistants = []
    if 'google' in product.name.lower() or any('google' in x.lower() for x in product.desc):
        assistants.append('Google Assistant')
    if 'alexa' in product.name.lower() or any('alexa' in x.lower() for x in product.desc):
        assistants.append('Alexa')
    if 'apple' in product.name.lower() or any('siri' in x.lower() for x in product.desc):
        assistants.append('Apple')
    if 'ifttt' in product.name.lower() or any('ifttt' in x.lower() for x in product.desc):
        assistants.append('IFTTT')
    product.assistant = assistants
    return product


def main():
    with open('./scrapes/products_11242018.pkl', 'rb') as f:
        product_list = pickle.load(f)

    invalid_list = []
    scraper = AmazonScraper()

    # Assign assistant to each product based on their name and desc
    # Store products with no name in invalid_list
    for product_id in product_list:
        if product_list[product_id].name:
            product_list[product_id] = find_assistant(product_list[product_id])
        else:
            invalid_list.append(product_id)

    # Retry fetching details for products in invalid_list
    # If still unavaulable 
    for product_id in invalid_list:
        product = scraper.get_product_details(product_id)
        if product.name:
            product_list[product_id] = find_assistant(product)
        else:
            del product_list[product_id]

    with open('./scrapes/products_11242018_cleaned.pkl', 'wb') as f:
            pickle.dump(product_list, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
        