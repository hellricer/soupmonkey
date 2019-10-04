# -*- coding: utf-8 -*-

def background(e, soup):
    e['style'] = 'background-color: white'

def remove(e, soup):
    e.decompose()

def border(e, soup):
    e['border'] = 1

def note(e, soup):
    e.insert(0, soup.new_string('» '))

modify = {
    'wikipedia.org' : [
        ('body', background),
        # infobox and other tables
        ('table.infobox, table.wikitable, table[role="presentation"]', border),
        # distinguish redirects, etc
        ('div[role=note]', note),
        # because of alt-text img captions are doubled
        ('div.thumbcaption', remove)
    ],
}
