#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url='https://www.practicepython.org'
r = requests.get(url)
r_html=r.text
#print(r_html)

soup = BeautifulSoup(r_html, "html.parser")
#print(soup.prettify())

myFile=open('mylist.html' ,'w')


for item in soup.select('li a'):
    myFile.write(str(item) + '\n')



