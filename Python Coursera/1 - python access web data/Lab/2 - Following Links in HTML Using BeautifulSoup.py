import re
import urllib.request
from bs4 import BeautifulSoup

#  http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Orlaithe.html
url = input('Enter the URL:')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))
check = cnt
a_tag = None
while cnt:
    print("Retrieving: ", end=" ")
    if cnt == check : 
        html = urllib.request.urlopen(url).read()
        print(url)
    else:
        url_name = re.findall('href="([^"]*)"', str(a_tag))[0]
        html = urllib.request.urlopen(url_name).read()
        print(url_name)
    
    soup = BeautifulSoup(html, 'html.parser')
    a_tag = soup('a')[pos-1]
    cnt -= 1
print(re.findall('.*([A-Z][a-z]+)[^.]', str(a_tag))[0])

