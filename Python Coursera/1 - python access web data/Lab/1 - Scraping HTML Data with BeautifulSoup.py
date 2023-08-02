import socket, re
import urllib.request
from bs4 import BeautifulSoup
#  http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# http://py4e-data.dr-chuck.net/comments_1860979.html (ends with 89)
url = input('Enter the URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

span_tags = soup('span')
print(sum([int(num) for num in re.findall('[0-9]+', (''.join([str(ele) for ele in span_tags])))]))
print(sum([sum([int(x) for x in re.findall('[0-9]+', str(ele))]) for ele in span_tags]))