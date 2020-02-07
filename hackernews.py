# -*- coding: utf-8 -*-

def hackernews_padding(e, soup):
    e['border'] = 1
    e['frame'] = 'void'
    e['rules'] = 'cols'
    for x in e.select('tr td.ind'):
        level = int(x.img['width']) / 40
        for y in range(int(level)):
            td = soup.new_tag('td')
            x.parent.insert(1, td)
        x.decompose()

def hackernews_votelink(e, soup):
    for x in e.select('.votearrow'):
        x.replaceWith(soup.new_string('▲'))
    if e.parent.select('.default'):
        e.parent.insert(0, e)

def hackernews_header(e, soup):
    e['border'] = 1
    e['frame'] = 'box'

modify = {
    'news.ycombinator.com' : [
        # remove logo
        ('img[src="y18.gif"]', lambda e, soup:
            e.parent.parent.decompose()),
        # nicer header
        ('#hnmain tr td table:nth-of-type(1)', hackernews_header),
        # indentation of comments
        ('tr.athing table', hackernews_padding),
        # vote arrows
        ('.votelinks', hackernews_votelink),
    ],
}
