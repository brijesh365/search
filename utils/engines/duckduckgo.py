import re
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

from utils.engines import abstract

API_URL = 'http://duckduckgo.com/html/?q={query}'
CLASS_REPR = 'DuckDuckGo'
RESULTS_COUNT = 10
HREF_REGEX = r'.*=([\w:/.]*)'


class DuckDuckGo(abstract.AbstractSearchEngine):
    @classmethod
    def __repr__(cls):
        return CLASS_REPR

    def search(self):
        try:
            with urllib.request.urlopen(API_URL.format(query=self.query)) as url:
                data = url.read()
        except Exception as e:
            print(e)
            result = ''
        else:
            result = BeautifulSoup(data, 'html5lib')
        return self.process_result(result)

    def process_result(self, result):
        return [
            {'link': re.findall(HREF_REGEX, urllib.parse.unquote(ele['href']))[0], 'text': ele.getText()}
            for ele in result.findAll('a', {'class': re.compile('result__a*')}, href=True)[:RESULTS_COUNT]
        ] if result else result
