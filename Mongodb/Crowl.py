from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.head.title
        print(title.get_text())
    except AttributeError as e:
        return None
    return title



def getLink(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs1 = BeautifulSoup(html.read(), 'html.parser')
        for link in bs1.find_all('a'):
            #print(type(link.get('href')))
            print(type(link.get('href')))
            getIntern(link.get('href'))
        '''print(linkers.find_all('href')[-1].extract())

        p = linkers.find_all('a[herf]')
        paragraphs = []
        for x in p:
            paragraphs.append(str(x))
        print(paragraphs)'''

    except Exception as e:
        return None
    return 0


def getIntern(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs1 = BeautifulSoup(html.read(), 'html.parser')
        for link in bs1.find_all('a'):
            #print(type(link.get('href')))
            getIntern(link.get('href'))



    except Exception as e:
        return None
    return 0

title = getTitle('http://www.iitg.ac.in/')
Link= getLink('http://www.iitg.ac.in/')
