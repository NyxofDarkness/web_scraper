import requests
from bs4 import BeautifulSoup

assert requests
assert BeautifulSoup

url = ""

def get_soup(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_citations_needed_count(url):
    soup = get_soup(url)
    results = soup.find_all('a', title = 'Wikipedia:Citation needed')
    count = len(results)
    print("Citations needed: ", count)
    return count

get_citations_needed_count(url)

counter = get_citations_needed_count('###')

def get_citations_needed_report(url):
    text = ""
    soup = get_soup(url)
    counter = get_citations_needed_count(url)
    results_count = f"Citations needed: {counter}"
    results = soup.find_all(class_='noprint Inline-Template-Fact')

    for i in results:
        p = i.find_parent('p')
        text += p.text.strip()
        text += '\n'*2

    print(text, results_count)
    return text
