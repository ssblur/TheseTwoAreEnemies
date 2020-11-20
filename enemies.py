#!/bin/env python
"""
Disney Wiki Enemies
Picks two random enemies from the Disney wiki.
"""
from html.parser import HTMLParser
import requests, os
from random import choice

class CharacterParser(HTMLParser):
    def __init__(self, find_enemies):
        self.link = ''
        self.name = ''
        self.image = ''

        # Enemies
        self.find_enemies = find_enemies
        self.depth = 0
        self.enemies = []
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attributes):
        if self.depth >= 1:
            self.depth = self.depth + 1

        # Find this page's name
        if tag == 'meta' and ('property', 'og:title') in attributes:
            for (k, v) in attributes:
                if k == 'content':
                    self.name = v
        
        # And it's image.
        if tag == 'meta' and ('property', 'og:image') in attributes:
            for (k, v) in attributes:
                if k == 'content':
                    self.image = v

        # Find this page's own link.
        if tag == 'link' and ('rel', 'canonical') in attributes:
            for (k, v) in attributes:
                if k == 'href':
                    self.link = v
                    break

        # Since we don't want to find enemies infinitely recursively, respect the option to skip this.
        if self.find_enemies:
            if ('data-source', 'enemies') in attributes:
                self.depth = 1
            if self.depth >=1 and tag == 'a':
                for (k, v) in attributes:
                    if k=='href':
                        self.enemies.append(v)

    def handle_endtag(self, tag):
        if self.depth >= 1:
            self.depth = self.depth - 1

def get_random_enemy(search = ''):
    character = CharacterParser(True)
    iteration = 0
    while character and len(character.enemies)==0:
        character = CharacterParser(True)
        if search != '':
            if iteration <= 10:
                match = requests.get(os.environ['WIKI_URL'] + '/api.php?action=opensearch&search={}&limit=10&namespace=0&format=json'.format(search))
                match = match.json()
                r = requests.get(match[3][searchIndex])
                iteration += 1
            else:
                r = requests.get(os.environ['WIKI_URL'] + '/wiki/Special:Random')
        else:
            r = requests.get(os.environ['WIKI_URL'] + '/wiki/Special:Random')
        character.feed(r.text)

    enemyLink = os.environ['WIKI_URL'] + choice(character.enemies)
    enemy = CharacterParser(False)
    r = requests.get(enemyLink)
    enemy.feed(r.text)

    return character, enemy

if __name__ == "__main__":
    print(get_random_enemy(input('Please enter who you want to target: ')))
