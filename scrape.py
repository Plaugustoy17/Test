import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import datetime
from time import time, mktime
website_name = 'https://nameberry.com/popular_names/Nameberry'
r_name = urllib.request.urlopen(website_name).read()
soup_name = BeautifulSoup(r_name ,'html.parser')
print(soup_name)
# test edit