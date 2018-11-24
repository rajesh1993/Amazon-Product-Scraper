class Product(object):
    def __init__(self):
        self._id = None
        self._name = None
        self._image = None
        self._rating = None
        self._seller = None
        self._price = None
        self._url = None
        self._desc = None
        self._category = None
        self._assistant = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
    
    @property
    def seller(self):
        return self._seller
    
    @seller.setter
    def seller(self, seller):
        self._seller = seller
    
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def assistant(self):
        return self._assistant

    @assistant.setter
    def assistant(self, assistant):
        self._assistant = assistant