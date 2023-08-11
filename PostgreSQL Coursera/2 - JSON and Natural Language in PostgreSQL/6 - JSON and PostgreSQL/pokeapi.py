
# https://www.pg4e.com/code/swapi.py
# https://www.pg4e.com/code/myutils.py

# If needed:
# https://www.pg4e.com/code/hidden-dist.py
# copy hidden-dist.py to hidden.py
# edit hidden.py and put in your credentials

# python3 swapi.py
# Pulls data from the swapi.py4e.com API and puts it into our swapi table
# import pip
# pip.main(['install', 'myutils'])
import psycopg2
import hidden
import time
import myutils
import requests
import json

def summary(cur) :
    total = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi;')
    todo = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status IS NULL;')
    good = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status = 200;')
    error = myutils.queryValue(cur, 'SELECT COUNT(*) FROM swapi WHERE status != 200;')
    print(f'Total={total} todo={todo} good={good} error={error}')

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

defaulturl = 'https://swapi.py4e.com/api/films/1/'
print('If you want to restart the spider, run')
print('DROP TABLE IF EXISTS swapi CASCADE;')
print(' ')

sql = '''
CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);
'''
print(sql)
cur.execute(sql)

for i in range(1, 101):
    url = f'https://pokeapi.co/api/v2/pokemon/{i}/'
    try:
        response = requests.get(url)
        json_data = response.json()
        print(json_data)
        # Convert the JSON dictionary to a JSON string
        json_string = json.dumps(json_data)
        
        # Insert JSON data into the 'pokeapi' table
        sql = 'INSERT INTO pokeapi (id, body) VALUES (%s, %s);'
        cur.execute(sql, (i, json_string))
        
        conn.commit()
        print(f'Retrieved and stored data for URL {url}')
    except Exception as e:
        print(f"Failed to retrieve or store data for URL {url}: {e}")
# Check to see if we have urls in the table, if not add starting points
# for each of the object trees


print('Closing database connection...')
conn.commit()
cur.close()
