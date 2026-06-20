import json
from dataclasses import dataclass
from urllib.parse import urlsplit
from html.parser import HTMLParser

@dataclass
class WebsiteData:
    url: str
    data: dict

class DataSifter:
    def __init__(self):
        self.websites = {}

    def extract_data(self, url: str, html: str) -> WebsiteData:
        class DataParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.data = {}

            def handle_data(self, data: str):
                self.data['text'] = data

        parser = DataParser()
        parser.feed(html)
        return WebsiteData(url, parser.data)

    def add_website(self, url: str, html: str):
        self.websites[url] = self.extract_data(url, html)

    def get_websites(self):
        return list(self.websites.values())

    def get_website(self, url: str):
        return self.websites.get(url)

    def supports_multiple_websites(self):
        return len(self.websites) > 1

    def handles_different_data_formats(self, url: str, data: dict):
        try:
            json.dumps(data)
            return True
        except TypeError:
            return False
