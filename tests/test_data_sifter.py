from data_sifter import WebScrapingEngine, ExtractedData, get_html, main
import pytest

def test_extract_data():
    url = 'https://example.com'
    engine = WebScrapingEngine(url)
    html = '<html><body><a href="https://example.com">Example</a></body></html>'
    extracted_data = engine.extract_data(html)
    assert extracted_data.url == url
    assert 'links' in extracted_data.data
    assert 'text' in extracted_data.data

def test_extract_data_empty_html():
    url = 'https://example.com'
    engine = WebScrapingEngine(url)
    html = ''
    extracted_data = engine.extract_data(html)
    assert extracted_data.url == url
    assert extracted_data.data == {}

def test_get_html():
    url = 'https://example.com'
    # Simulate getting HTML from a URL
    html = '<html><body><a href="https://example.com">Example</a></body></html>'
    assert get_html(url) == html

def test_main():
    # Test main function
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() != ''

def test_extracted_data_class():
    url = 'https://example.com'
    data = {'links': ['https://example.com'], 'text': 'Example'}
    extracted_data = ExtractedData(url, data)
    assert extracted_data.url == url
    assert extracted_data.data == data
