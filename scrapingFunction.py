# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:49:36 2020

@author: benja
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


'''
função getTitle para obeter titulos de paginas web
'''

def getTittle(url):
    try:
        html =urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return title
    return title

title = getTittle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title não encontrado')
else:
    print(title)