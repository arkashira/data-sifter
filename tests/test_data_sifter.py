import pytest
from data_sifter import DataSifter, Page

def test_classify_product():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/product',
        dom_structure={'types': ['product']},
        microdata={'types': ['product']}
    )
    assert data_sifter.classify(page) == 'product'

def test_classify_article():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/article',
        dom_structure={'types': ['article']},
        microdata={'types': ['article']}
    )
    assert data_sifter.classify(page) == 'article'

def test_classify_landing():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/landing',
        dom_structure={'types': ['landing']},
        microdata={'types': ['landing']}
    )
    assert data_sifter.classify(page) == 'landing'

def test_classify_blog():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/blog',
        dom_structure={'types': ['blog']},
        microdata={'types': ['blog']}
    )
    assert data_sifter.classify(page) == 'blog'

def test_classify_profile():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/profile',
        dom_structure={'types': ['profile']},
        microdata={'types': ['profile']}
    )
    assert data_sifter.classify(page) == 'profile'

def test_classify_generic():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/generic',
        dom_structure={'types': []},
        microdata={'types': []}
    )
    assert data_sifter.classify(page) == 'generic'

def test_log_confidence_score_high():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/product',
        dom_structure={'types': ['product']},
        microdata={'types': ['product']}
    )
    data_sifter.log_confidence_score(page, 'product')

def test_log_confidence_score_low():
    data_sifter = DataSifter()
    page = Page(
        url='https://example.com/product',
        dom_structure={'types': []},
        microdata={'types': []}
    )
    data_sifter.log_confidence_score(page, 'product')
