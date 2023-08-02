import sqlite3
import mysql.connector as connector
import urllib.request, urllib
import requests

def read_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        if response.headers.get("content-type") == "text/plain":
            return response.text
        else:
            print(f"The URL '{url}' does not contain a plain text file.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')

    cur.execute('''
    CREATE TABLE Counts (email VARCHAR(255), count INTEGER)''')

    fname = input('Enter file URL: ') #https://www.py4e.com/code3/mbox.txt?PHPSESSID=a2d32dfab7514fe44c29e10d52fed8a8
    fh = read_text_from_url(fname).split('\n')
    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        email = pieces[1]
        # print(type(email))
        cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email, ))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                        (email, ))
        conn.commit()

    # https://www.sqlite.org/lang_select.html
    # sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

    # for row in cur.execute(sqlstr):
    #     print(str(row[0]), row[1])

    cur.close()