import os
import re
import bs4

modules = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    modules.append(__import__(module[:-3], locals(), globals()))
del module

def _modifier(url, html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for module in modules:
        for pattern in filter(lambda pattern: pattern in url, module.modify):
            for selector in module.modify[pattern]:
                [selector[1](e, soup) for e in soup.select(selector[0])]
    return str(soup)

def _replacer(url, html):
    new = html
    for module in modules:
        for pattern in filter(lambda pattern: pattern in url, module.replace):
            for replacement in module.replace[pattern]:
                new = re.sub(replacement[0], replacement[1], new)
    return new

def infect(url, html):
    html = _modifier(url, html)
    html = _replacer(url, html)
    return html
