import re
import json
import requests
from bs4 import BeautifulSoup


def get_og(url):
    r = requests.get(url)
    doc = BeautifulSoup(r.text, "lxml")
    ogs = doc.html.head.findAll(property=re.compile(r'^og'))
    d = {og["property"][3:]: og["content"] for og in ogs}
    return d
