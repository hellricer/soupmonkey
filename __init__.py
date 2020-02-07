import os
import re
import bs4
from importlib import import_module

modules = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    modules.append(import_module('.' + module[:-3], package = 'soupmonkey'))
    del module

def _substitute(url, html):
    target = html
    for module in modules:
        try:
            for p in filter(lambda pattern: re.search(pattern, url), module.substitute):
                for substitute in module.substitute[p]:
                    target = re.sub(substitute[0], substitute[1], target, flags=(re.DOTALL + re.I))
        except AttributeError:
            pass
    return target

def inject(f):
    def _modify(url, html):
        soup = bs4.BeautifulSoup(_substitute(url, html), 'html.parser')
        for module in modules:
            try:
                for p in filter(lambda pattern: re.search(pattern, url), module.modify):
                    for selector in module.modify[p]:
                        [selector[1](e, soup) for e in soup.select(selector[0])]
            except AttributeError:
                pass
        return f(url, str(soup))
    return _modify
