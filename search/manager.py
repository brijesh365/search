import functools

from django.db import models

from search.queryset import QueryQuerySet, ResultQuerySet


class BaseQueryManager(models.Manager):

    def get_queryset(self, queryset_class):
        return queryset_class(self.model, using=self._db)


class QueryManager(BaseQueryManager):
    use_in_migrations = True
    queryset_class = QueryQuerySet

    def get_by_query(self, query):
        return self.get_queryset(self.queryset_class).get_by_query(query)

    def is_query_exists(self, query):
        return self.get_queryset(self.queryset_class).is_query_exists(query)

    def get_search_queries(self):
        return self.get_queryset(self.queryset_class).get_search_queries()

    def create(self, **fields):
        query = fields.pop('query')
        if not query:
            raise ValueError('Query is mandatory')
        query = self.model(query=query.lower())
        query.save(using=self._db)
        return query


class ResultManager(BaseQueryManager):
    use_in_migrations = True
    queryset_class = ResultQuerySet

    @functools.lru_cache()
    def get_search_results(self, query):
        return self.get_queryset(self.queryset_class).get_search_results(query)

    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        return self.get_queryset(self.queryset_class).bulk_create(objs, batch_size, ignore_conflicts)
