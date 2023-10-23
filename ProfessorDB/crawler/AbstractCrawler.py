from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from crawler.item_handlers.ItemHandler import ItemHandler

class AbstractCrawler(ABC):
    def __init__(self, item_handler: ItemHandler):
        self.item_handler = item_handler

    # if you need to send a custom non-Raw GET request to a target,
    # ... just do fetch=False, and pass the response object instead of url.
    def crawl(self, target, fetch=True):
        if fetch:
            response = requests.get(target)
        else:
            response = target
        # performing the crawl event chain
        self.collect(
            self.process(
                self.parse(response)
            )
        )

    def parse(self, response):
        return BeautifulSoup(response.text, 'html.parser')

    @abstractmethod
    def process(self, soup: BeautifulSoup):
        # should yield none, one, or multiple items.
        pass

    def collect(self, items):
        # process() didn't yield any items:
        if items is None:
            return

        for item in items:
            self.item_handler.handle(item)