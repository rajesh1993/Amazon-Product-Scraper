from lxml import html  
import csv,os,json
import requests
from time import sleep
import random
import base64
import ast
from product import Product
from xpath import XPathCommands
import pickle
from os import listdir

class AmazonScraper(object):
    
    def __init__(self, headerfile='user-agents.txt'):
        self.xpath = XPathCommands()
        self.headers = self.get_headers(headerfile)
        
    def get_headers(self, file):
        '''Returns a list of user-agents from the input file'''
        with open(file, 'r') as f:
            headers = ast.literal_eval(f.read())
        return headers

    def get_html(self, url):
        '''Returns the html content of the given url'''
        user_agent = random.choice(self.headers)
        page = requests.get(url,headers={'User-Agent': user_agent})
        return page

    def get_items_from_page(self, url):
        '''Obtains the list of items in the product list page-url specified'''
        page = self.get_html(url)
        doc = html.fromstring(page.content)
        for item in doc.xpath(self.xpath.item_list):
            yield str(item)
    
    def __get_product_name(self, doc):
        '''Uses the lxml document to fetch product name'''
        product_name = doc.xpath(self.xpath.item_name)
        if product_name:
            product_name = product_name[0].strip()
        return product_name

    def __get_product_price(self, doc):
        '''Uses the lxml doc to fetch product price'''
        product_price = doc.xpath(self.xpath.item_price)
        if product_price and len(product_price) == 1:
            product_price = float(product_price[0].strip()[1:].replace(',', ''))
        return product_price

    def __get_product_rating(self, doc):
        '''Uses the lxml doc to fetch product rating'''
        product_rating = doc.xpath(self.xpath.item_rating)
        if product_rating:
            product_rating = float(product_rating[0].strip().split()[0])
        return product_rating
    
    def __get_product_image(self, doc):
        '''Uses the lxml doc to fetch product image as base64 code'''
        product_image = doc.xpath(self.xpath.item_image)
        if product_image:
            if product_image[0].startswith('http'):
                product_image = product_image[0]
            else:
                base64_code = product_image[0].split(',')[1]
                product_image = base64_code.split('\n')[0]
        return product_image

    def __get_product_seller(self, doc):
        '''Uses the lxml doc to fetch product seller'''
        product_seller = doc.xpath(self.xpath.item_seller)
        if product_seller:
            product_seller = product_seller[0]
        return product_seller
    
    def __get_product_desc(self, doc):
        '''Fetches the product description from the doc'''
        product_desc = doc.xpath(self.xpath.item_desc)
        if product_desc:
            product_desc = [x.strip() for x in product_desc]
            product_desc = [x for x in product_desc if len(x) > 2]
        return product_desc

    def get_product_details(self, product_id):
        '''Fetch product details from page'''
        product = Product()
        product.id = product_id
        product.url = "https://www.amazon.com/dp/" + product.id
        
        # Get page
        page = self.get_html(product.url)
        doc = html.fromstring(page.content)
        
        # Get item details
        product.name = self.__get_product_name(doc)
        product.price = self.__get_product_price(doc)
        product.rating = self.__get_product_rating(doc)
        product.image = self.__get_product_image(doc)
        product.seller =  self.__get_product_seller(doc)
        product.desc = self.__get_product_desc(doc)

        return product


def main():
    scraper = AmazonScraper()
    product_list = {}

    for url_file in listdir('./url'):
        product_count = 0
        with open('./url/' + url_file, 'r') as file:
            url_list = file.readlines()

        for url in url_list:
            item_ids = scraper.get_items_from_page(url)

            for item_id in item_ids:
                product = scraper.get_product_details(item_id)
                product.category = url_file.split('.')[0]
                product_list[item_id] = product
                product_count += 1

        print('Completed scraping %s. Collected %d products.' % (url_file, product_count))

    with open('./scrapes/products_11242018.pkl', 'wb') as f:
        pickle.dump(product_list, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()





