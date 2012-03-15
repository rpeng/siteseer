import random

import cherrypy
import memcache

class SiteSeer:
    mc = memcache.Client(['localhost:11211'])
    def index(self):
        count = int(SiteSeer.mc.get('site_count'))
        index = random.randrange(0, count)
        url = SiteSeer.mc.get(str(index))

        raise cherrypy.HTTPRedirect(url)

    index.exposed = True

cherrypy.quickstart(SiteSeer())
