import urllib.request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1860981.xml (Sum ends with 36)
url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read().decode()
tree = ET.fromstring(html)
print(sum([int(ele.text) for ele in tree.findall('.//count')]))

