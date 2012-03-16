import memcache

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('sitemap.0.xml').read())
results = soup.find_all('loc')

mc = memcache.Client(['localhost:11211'])

_count = 0

for i in results:
    mc.set(str(_count),i.text)
    _count += 1

print _count
mc.set('site_count', _count)
