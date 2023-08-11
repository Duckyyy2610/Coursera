# Import the necessary libraries
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
import time
import copy
import hidden
import uuid
import json
import hashlib

# Prompt the user to enter the book file (i.e., pg18866.txt as the default)
bookfile = input("Enter book file (i.e. pg18866.txt): ")
if bookfile == '':
    bookfile = 'pg18866.txt'

# Make sure we can open the file
fhand = open(bookfile, encoding="utf-8")

# Load the Elasticsearch connection details from the hidden file
secrets = hidden.elastic()

# Connect to Elasticsearch
es = Elasticsearch(
    [secrets['host']],
    http_auth=(secrets['user'], secrets['pass']),
    url_prefix=secrets['prefix'],
    scheme=secrets['scheme'],
    port=secrets['port'],
    connection_class=RequestsHttpConnection,
)
indexname = secrets['user']

# Start fresh: delete the existing index
res = es.indices.delete(index=indexname, ignore=[400, 404])
print("Dropped index", indexname)
print(res)

# Create a new index with the specified name
res = es.indices.create(index=indexname)
print("Created the index...")
print(res)

para = ''
chars = 0
count = 0
pcount = 0

# Iterate over the lines in the book file
for line in fhand:
    count = count + 1
    line = line.strip()
    chars = chars + len(line)

    # If the line is empty and para is empty, skip
    if line == '' and para == '':
        continue

    # If the line is empty, it's the end of a paragraph
    if line == '':
        pcount = pcount + 1
        doc = {
            'offset': pcount,
            'content': para
        }

        # Use SHA256 of the entire document as the primary key
        m = hashlib.sha256()
        m.update(json.dumps(doc).encode())
        pkey = m.hexdigest()

        # Index the paragraph in Elasticsearch
        res = es.index(index=indexname, id=pkey, body=doc)

        print('Added document', pkey)

        if pcount % 100 == 0:
            print(pcount, 'loaded...')
            time.sleep(1)

        para = ''
        continue

    # Append the line to the current paragraph
    para = para + ' ' + line

# Refresh the index to make the data available for searching
res = es.indices.refresh(index=indexname)
print("Index refreshed", indexname)
print(res)

print(' ')
print('Loaded', pcount, 'paragraphs', count, 'lines', chars, 'characters')
