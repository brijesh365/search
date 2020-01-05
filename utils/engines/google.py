from googleapiclient.discovery import build

from utils.engines import abstract

CLASS_REPR = 'Google'
RESULTS_COUNT = 10
API_KEY = "AIzaSyDHVI8Pvfh5_bgNmZXVBs-EfOq0Sbr4ydk"
CSE_ID = "001964664684553019863:8lmblvhbapf"


class Google(abstract.AbstractSearchEngine):
    @classmethod
    def __repr__(cls):
        return CLASS_REPR

    def search(self):
        try:
            service = build('customsearch', 'v1', developerKey=API_KEY, cache_discovery=False)
            response = service.cse().list(q=self.query, cx=CSE_ID, num=RESULTS_COUNT).execute()
        except Exception as e:
            print(e)
            result = ''
        else:
            result = response['items']
        return self.process_result(result)

    def process_result(self, result):
        return [
            {'link': ele['link'], 'text': ele['title']}
            for ele in result
        ] if result else result
