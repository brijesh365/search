from django.db import models

from search.constants import COMPLETED


class QueryQuerySet(models.QuerySet):
    def get_search_queries(self):
        return self.filter().order_by('-added_on')[:10]

    def is_query_exists(self, query):
        return self.get_by_query(query).exists()

    def get_by_query(self, query):
        return self.filter(query=query)


class ResultQuerySet(models.QuerySet):

    def get_search_results(self, query):
        return self.filter(query__query=query, query__status=COMPLETED)

    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        return super().bulk_create(objs, batch_size, ignore_conflicts)