import requests
from bs4 import BeautifulSoup

from utils.engines import abstract

API_URL = 'https://en.wikipedia.org/wiki/{query}'
CLASS_REPR = 'Wikipedia'
RESULTS_COUNT = 2


class Wikipedia(abstract.AbstractSearchEngine):
    @classmethod
    def __repr__(cls):
        return CLASS_REPR

    def search(self):
        self.url = API_URL.format(query=self.query)
        try:
            response = requests.get(self.url)
        except Exception as e:
            print(e)
            result = ''
        else:
            result = BeautifulSoup(response.text, 'html5lib')
        return self.process_result(result)

    def process_result(self, result):
        if result:
            paragraphs = result.find_all('p', attrs={'class': None})
            paras = '\n'.join([para.getText() for para in paragraphs[:2]])
            return [{'link': self.url, 'text': paras}]
        return ''
