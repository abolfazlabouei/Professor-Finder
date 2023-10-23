from abc import ABC, abstractmethod

class ItemHandler(ABC):

    def handle(self, item):
        self.preprocess_item(item)
        if self.item_exists(item):
            return
        self.collect_item(item)

    # in case any pre-processing is needed; e.g. setting static fields
    @abstractmethod
    def preprocess_item(self, item):
        pass

    # final part of the data-flow
    # this is where the storing process happens (like passing the item to database)
    @abstractmethod
    def collect_item(self, item):
        pass

    # a boolean function, for avoiding duplicate data
    @abstractmethod
    def item_exists(self, item):
        return True