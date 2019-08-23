import os, re, sqlite3
from bs4 import BeautifulSoup

conn = sqlite3.connect('symfony-docs.docset/Contents/Resources/docSet.dsidx')
cur = conn.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except Exception:
    pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = 'symfony-docs.docset/Contents/Resources/Documents'

page = open(os.path.join(docpath, 'genindex.html')).read()
soup = BeautifulSoup(page)

all_pages = re.compile('.*')
for tag in soup.find_all('a', {'href': all_pages}):
    name = tag.text.strip()
    if len(name) > 1:
        path = tag.attrs['href'].strip()
        try:
            tmp_path = re.sub(r'#.*', '', path)
            print(tmp_path)
            tmp_page = open(os.path.join(docpath, tmp_path)).read()
            tmp_soup = BeautifulSoup(tmp_page)
            title = tmp_soup.find('title');
            name = title.text.strip()
        except Exception:
            pass
        if path != 'index.html':
            cur.execute('SELECT * FROM searchIndex WHERE name=?', (name,))
            data = cur.fetchone()
            if not data:
                cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Guide', path))
                print('name: %s, path: %s' % (name, path))

conn.commit()
conn.close()
