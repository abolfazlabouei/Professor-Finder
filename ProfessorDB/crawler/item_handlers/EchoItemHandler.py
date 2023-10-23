from crawler.item_handlers.ItemHandler import ItemHandler

class EchoItemHandler(ItemHandler):
    def preprocess_item(self, item):
        pass

    def item_exists(self, item):
        return False

    def collect_item(self, item):
        print(item)