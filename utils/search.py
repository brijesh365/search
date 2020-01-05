from search import constants
from search import models
from utils.engines import search_engines


class Search:
    def __init__(self, query):
        self.query = query

    def search(self):
        query_object = models.Query.objects.get_by_query(self.query)
        data = []
        for engine_class in search_engines:
            search_engine = engine_class(self.query)
            result = search_engine.search()
            data.append(
                models.Result(**{'query': query_object[0], 'engine': engine_class.__repr__(), 'result': result})
            )
        self.update_records(query_object, data)

    def update_records(self, query_object, data):
        models.Result.objects.bulk_create(data)
        query_object.update(status=constants.COMPLETED)
