#!/bin/env python
"""
Disney Wiki Enemies
Picks two random enemies from the Disney wiki.
"""
from html.parser import HTMLParser
import requests
from random import choice

class EnemySectionExtractor(HTMLParser):
    def __init__(self):
        self.depth = 0
        self.enemies = []
        self.link = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attributes):
        if self.depth >= 1:
            self.depth = self.depth + 1
        if tag == 'link' and ('rel', 'canonical') in attributes:
            for (k, v) in attributes:
                if k == 'href':
                    self.link = v
        if ('data-source', 'enemies') in attributes:
            self.depth = 1
        if self.depth >=1 and tag == 'a':
            for (k, v) in attributes:
                if k=='href':
                    self.enemies.append(v)

    def handle_endtag(self, tag):
        if self.depth >= 1:
            self.depth = self.depth - 1

def get_random_enemy():
    parser = EnemySectionExtractor()
    while parser and len(parser.enemies)==0:
        parser = EnemySectionExtractor()
        r = requests.get('https://disney.fandom.com/wiki/Special:Random')
        parser.feed(r.text)
    message = parser.link + ' and https://disney.fandom.com/' + choice(parser.enemies) + ' are enemies.'
    return message

if __name__ == "__main__":
    print(get_random_enemies())