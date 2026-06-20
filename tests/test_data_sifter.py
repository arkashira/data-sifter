from data_sifter import DataSifter, WebsiteData
import pytest

def test_extract_data():
    sifter = DataSifter()
    url = "https://example.com"
    html = "<html><body>Hello World!</body></html>"
    data = sifter.extract_data(url, html)
    assert isinstance(data, WebsiteData)
    assert data.url == url
    assert data.data == {'text': 'Hello World!'}

def test_add_website():
    sifter = DataSifter()
    url = "https://example.com"
    html = "<html><body>Hello World!</body></html>"
    sifter.add_website(url, html)
    assert url in sifter.websites

def test_get_websites():
    sifter = DataSifter()
    url1 = "https://example1.com"
    url2 = "https://example2.com"
    html1 = "<html><body>Hello World!</body></html>"
    html2 = "<html><body>Foo Bar!</body></html>"
    sifter.add_website(url1, html1)
    sifter.add_website(url2, html2)
    websites = sifter.get_websites()
    assert len(websites) == 2

def test_get_website():
    sifter = DataSifter()
    url = "https://example.com"
    html = "<html><body>Hello World!</body></html>"
    sifter.add_website(url, html)
    website = sifter.get_website(url)
    assert website is not None
    assert isinstance(website, WebsiteData)

def test_supports_multiple_websites():
    sifter = DataSifter()
    url1 = "https://example1.com"
    url2 = "https://example2.com"
    html1 = "<html><body>Hello World!</body></html>"
    html2 = "<html><body>Foo Bar!</body></html>"
    sifter.add_website(url1, html1)
    sifter.add_website(url2, html2)
    assert sifter.supports_multiple_websites()

def test_handles_different_data_formats():
    sifter = DataSifter()
    url = "https://example.com"
    data = {'key': 'value'}
    assert sifter.handles_different_data_formats(url, data)

def test_handles_different_data_formats_failure():
    sifter = DataSifter()
    url = "https://example.com"
    data = {'key': lambda x: x}
    assert not sifter.handles_different_data_formats(url, data)
