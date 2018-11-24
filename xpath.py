class XPathCommands(object):
    def __init__(self):
        self._item_list = '//*/@data-asin'
        self._item_name = '//*[@id="productTitle"]/text()'
        self._item_image = '//*[@id="landingImage"]/@src'
        self._item_rating = '//*[@id="acrPopover"]/@title'
        # self._item_price = '//*[@id="priceblock_ourprice"]/text()'
        self._item_price ='//span[starts-with(@id,"priceblock")]/text()'
        self._item_seller = '//*[@id="bylineInfo"]/text()'
        self._item_desc = '//*[@id="feature-bullets"]/ul/li/span//text()'
    
    @property
    def item_name(self):
        return self._item_name

    @property
    def item_image(self):
        return self._item_image

    @property
    def item_rating(self):
        return self._item_rating

    @property
    def item_price(self):
        return self._item_price
    
    @property
    def item_seller(self):
        return self._item_seller
    
    @property
    def item_list(self):
        return self._item_list

    @property
    def item_desc(self):
        return self._item_desc