import requests
from bs4 import BeautifulSoup

assert requests
assert BeautifulSoup

url = "https://en.wikipedia.org/wiki/Saudi_Arabian-led_intervention_in_Yemen"


def get_citations_needed_count(url):

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find(id = 'mw-content-text')
    citation_count = result.find_all('a', title="Wikipedia:Citation needed" )
    return len(citation_count)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_count = soup.find_all('a', title="Wikipedia:Citation needed")
    text = []
    show_text = ''
    for text_break in citation_count:
        text.append(text_break.find_parents('p')[0].text.strip())
  
    for i in text:
        show_text += f'citation needed for: {i}'
    return show_text

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))
