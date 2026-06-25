import json
from dataclasses import dataclass
from urllib.parse import urljoin
from html.parser import HTMLParser

@dataclass
class ExtractedData:
    url: str
    data: dict

class WebScrapingEngine:
    def __init__(self, url):
        self.url = url
        self.data = {}

    def extract_data(self, html):
        parser = HTMLParser()
        parser.handle_starttag = self.handle_starttag
        parser.handle_endtag = self.handle_endtag
        parser.handle_data = self.handle_data
        parser.feed(html)
        return ExtractedData(self.url, self.data)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.data['links'] = self.data.get('links', []) + [attr[1]]

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self.data['text'] = self.data.get('text', '') + data

def get_html(url):
    # Simulate getting HTML from a URL
    return '<html><body><a href="https://example.com">Example</a></body></html>'

def main():
    url = 'https://example.com'
    engine = WebScrapingEngine(url)
    html = get_html(url)
    extracted_data = engine.extract_data(html)
    print(json.dumps(extracted_data.__dict__))

if __name__ == '__main__':
    main()
