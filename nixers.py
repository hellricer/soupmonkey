# -*- coding: utf-8 -*-

def remove(e, soup):
    e.decompose()

def border(e, soup):
    e['border'] = 1
    e['rules'] = 'groups'

modify = {
    'nixers.net' : [
        ('table.postbit_table', border),
        ('span.usernames', remove),
    ],
    'nixers.net/member.php' : [
        ('table.tborder', border),
    ],
}
