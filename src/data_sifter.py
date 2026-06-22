import json
from dataclasses import dataclass
from urllib.parse import urlparse
from collections import Counter

@dataclass
class Page:
    url: str
    dom_structure: dict
    microdata: dict

class DataSifter:
    def __init__(self):
        self.heuristics = {
            'product': self.is_product,
            'article': self.is_article,
            'landing': self.is_landing,
            'blog': self.is_blog,
            'profile': self.is_profile,
            'generic': self.is_generic
        }

    def classify(self, page: Page):
        scores = {}
        for page_type, heuristic in self.heuristics.items():
            scores[page_type] = heuristic(page)
        return max(scores, key=scores.get)

    def is_product(self, page: Page):
        return self.has_microdata(page, 'product') or self.has_dom_structure(page, 'product')

    def is_article(self, page: Page):
        return self.has_microdata(page, 'article') or self.has_dom_structure(page, 'article')

    def is_landing(self, page: Page):
        return self.has_microdata(page, 'landing') or self.has_dom_structure(page, 'landing')

    def is_blog(self, page: Page):
        return self.has_microdata(page, 'blog') or self.has_dom_structure(page, 'blog')

    def is_profile(self, page: Page):
        return self.has_microdata(page, 'profile') or self.has_dom_structure(page, 'profile')

    def is_generic(self, page: Page):
        return True

    def has_microdata(self, page: Page, page_type: str):
        return page_type in page.microdata.get('types', [])

    def has_dom_structure(self, page: Page, page_type: str):
        return page_type in page.dom_structure.get('types', [])

    def log_confidence_score(self, page: Page, page_type: str):
        scores = {}
        for heuristic in self.heuristics.values():
            scores[heuristic.__name__] = heuristic(page)
        confidence_score = sum(scores.values()) / len(scores)
        if confidence_score >= 0.7:
            print(f'Confidence score for {page_type}: {confidence_score:.2f}')
        else:
            print(f'Confidence score for {page_type} is low: {confidence_score:.2f}')

def main():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/product',
        dom_structure={'types': ['product']},
        microdata={'types': ['product']}
    )
    page_type = data_sifter.classify(page)
    data_sifter.log_confidence_score(page, page_type)
    print(f'Classified as: {page_type}')

if __name__ == '__main__':
    main()
