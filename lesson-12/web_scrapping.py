from bs4 import BeautifulSoup

html_conent = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BeautifulSoup(html_conent, 'html.parser')

title = soup.title

# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# print(soup.get_text())

# print(soup.prettify())

# tag = soup.a
# print(tag)
# print(tag['class'])
# print(tag["href"])
# print(tag["id"])
# tag['id'] = "link0"
# print(tag['id'])

import requests
from bs4 import BeautifulSoup

url = 'https://data.worldbank.org/country'
res = requests.get(url)
res.status_code

soup = BeautifulSoup(res.content)
print(soup)

countries = {}

sections = soup.find_all('section')
for section in sections:
    title = section.find('h3')
    countries[title.text] = []
    # print(title.text)
    names = section.find_all('a')
    for name in names:
        countries[title.text].append(name.text)
        print('\t', name.text)