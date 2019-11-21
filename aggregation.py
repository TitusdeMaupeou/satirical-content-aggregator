import requests
import json
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

urls = []
html_obj = {}
article_list = []

with open('titles.json') as file:
    data = json.load(file)

params = []
for k,v in data.items():
    urls.append(k)
    for item in v:
        if item not in params:
            params.append(item)

def get_html(url, index):
    d = {}
    _class = data[url]['article']
    for param in params:
        d[param] = data[url][param]
    for articles in soup.find_all(class_ = _class):
        article_info = {}
        for k,v in d.items():
            if articles.find(class_ =v):
                if articles.find(class_=v).get_text():
                    article_info[k] = articles.find(class_=v).get_text()
                if articles.find('img'):
                    img = articles.find('img')
                    article_info['img'] = img['src']
        article_list.append(article_info)

for index, url in enumerate(urls):
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        get_html(url, index)