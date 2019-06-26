# -*- coding: utf-8 -*-

def remove(e, soup):
    e.decompose()

def images(e, soup):
    img = e.find_all('img')[0]
    img['alt'] = e.figcaption.text
    e.figcaption.decompose()

def to_span(e, soup):
    e.name = "span"
    e.span.a.string = " • ".decode('utf-8') + e.span.a.string

def add_dot(e, soup):
    e.content = " • ".decode('utf-8') or u'None' + e.content

def add_background(e, soup):
    e['style']="background-color: white"

modify = {
    'medium.com' : [
        ('input', remove),
        ('a img', remove),
        ('button', remove),
        ('a.button', remove),
        ('span.u-textScreenReader', remove),
        ('body', add_background),
        ('figure', images),
        ('.link', add_dot),
    ],
}

substitute = {}
