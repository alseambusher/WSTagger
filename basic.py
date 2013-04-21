import urllib
import urllib2
import json
#google search
def gsearch(searchfor):
    query = urllib.urlencode({'q': searchfor.lower()})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_request=urllib2.Request(url)
    search_request.add_header('User-Agent',
                              'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) '
                              'Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')
    search_request.add_header('Referer','http://www.python.org/')
    search_response = urllib2.urlopen(search_request)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    return data

