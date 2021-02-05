from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
import pytest


def test_import():
    assert get_citations_needed_count
    assert get_citations_needed_report

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    
def test_count():
    # used a different wiki page from the assignment to make sure it worked properly!
    assert get_citations_needed_count(url) == 5

def test_one():
    actual = get_citations_needed_report(url)
    expected = '"citation nee...s population."'
    assert expected == actual
