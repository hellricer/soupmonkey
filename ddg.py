# -*- coding: utf-8 -*-

def background(e, soup):
    e['style'] = 'background-color: white'

def border(e, soup):
    e['border'] = 1

modify = {
    'duckduckgo.com' : [
        ('body', background),
        # tables
        ('.extra table', border)
    ],
}
