import pymongo
from crawler.item_handlers.ItemHandler import ItemHandler

"""
This handler is structured based on a document schema.
We tend to store every record of a "professor" with this schema:
{Name, Email, Area of expertise, College, Department}
"""
class MongoDBHandler(ItemHandler):

    def __init__(self, mongo_uri="mongodb://localhost:27017/", mongo_db="professors_db", mongo_collection="professors"):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = mongo_collection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.static_fields = {}

    def goodbye(self):
        self.client.close()

    def preprocess_item(self, item: dict):
        item.update(self.static_fields)

    # accepts a dict
    def collect_item(self, item: dict):
        self.db[self.collection_name].insert_one(item)

    # accepts a dict too
    # checks the existence based on Name
    def item_exists(self, item):
        return self.db[self.collection_name].find({'Name': item['Name'], 'College': item['College']}).count() > 0