import re
import json
import requests
from bs4 import BeautifulSoup

r = requests.get("https://github.com/Dineshkarthik/open_graph")

doc = BeautifulSoup(r.text, "lxml")
ogs = doc.html.head.findAll(property=re.compile(r'^og'))
d = {og["property"][3:]: og["content"] for og in ogs}
