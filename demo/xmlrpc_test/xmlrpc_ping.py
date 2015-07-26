import re
from xmlrpc.client import ServerProxy

# ping weblog to make your website be indexed

my_url='https://utcc.utoronto.ca/~cks/space/blog/python/PingingWeblogsInPython'
weblog_rpc_ping_address='http://rpc.weblogs.com/RPC2'


def ping(webname, hosturl, linkurl):
    rpc_server = ServerProxy(weblog_rpc_ping_address)
    result = rpc_server.weblogUpdates.extendedPing(webname, hosturl, linkurl)

    print(result)
    if result.get('flerror', False) == True:
        print('ping error')
    else:
        print('ping success')

def get_url(url):
    host_re = re.compile(r'^https?://(.*?)($|/)', re.IGNORECASE)
    return host_re.search(url).group(0)

webname = my_url.split('.')[1]
hosturl = get_url(my_url)
ping(webname, hosturl, my_url)
