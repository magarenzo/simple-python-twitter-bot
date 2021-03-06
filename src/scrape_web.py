#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

# 46 tweets generated below

file_path = './facts.txt'

# 11 tweets
url = 'http://www.sciencekids.co.nz/sciencefacts/animals/bird.html'
page = requests.get(url)
c = page.content
soup = BeautifulSoup(c)

ul = soup.find('ul', {'class': 'style33'})
children = ul.findChildren('p')
f = open(file_path, 'w')
for child in children:
        line = child.text
        fact = line.encode('ascii', 'ignore')
        count = len(fact)
        if (count <= 140):
                f.write(fact + "\n")
f.close()

# Store facts already written from the first scrape
f = open(file_path, 'r')
lines = f.readlines()
f.close()

# 12 tweets
url = 'https://www.mspca.org/pet_resources/interesting-facts-about-birds/'
page = requests.get(url)
c = page.content
soup = BeautifulSoup(c)

div = soup.find('div', {'class': 'leftColumn'})
children = div.findChildren('p')
f = open(file_path, 'w')
for line in lines:
        f.write(line)
for child in children:
        line = child.text
        fact = line.encode('ascii', 'ignore')
        count = len(fact)
        if (count <= 140):
                f.write(fact + "\n")
f.close()

# Store facts already written from the first scrape and second scrapes
f = open(file_path, 'r')
lines = f.readlines()
f.close()

# 12 tweets
url = 'http://www.peteducation.com/article.cfm?c=15+1794&aid=179'
page = requests.get(url)
c = page.content
soup = BeautifulSoup(c)

div = soup.find('div', {'class': 'artext'})
children = div.findChildren('p')
f = open(file_path, 'w')
for line in lines:
        f.write(line)
for child in children:
        line = child.text
        fact = line.encode('ascii', 'ignore')
        count = len(fact)
        if (count <= 140):
                f.write(fact + "\n")
f.close()

# Store facts already written from the first, second and third scrapes
f = open(file_path, 'r')
lines = f.readlines()
f.close()

# 11 tweets
url = 'https://kidskonnect.com/animals/bird/'
page = requests.get(url)
c = page.content
soup = BeautifulSoup(c)

amount = 0

div = soup.find('div', {'class': 'entry-content'})
children = div.findChildren('li')
f = open(file_path, 'w')
for line in lines:
        f.write(line)
        amount += 1
for child in children:
        line = child.text
        fact = line.encode('ascii', 'ignore')
        count = len(fact)
        if (count <= 140):
                f.write(fact + "\n")
                amount += 1
f.close()

print amount,'facts written to',file_path,'for tweeting'
