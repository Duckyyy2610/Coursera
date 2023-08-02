import urllib.request, urllib.parse
import json

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1860982.json (Sum ends with 54)

url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read().decode()

js = json.loads(html)
print(sum([int(x["count"]) for x in js["comments"]]))