from django.shortcuts import render
from django.views import View

from search import models
from utils import queue
from utils import search as search_util


class Query(View):
    def get(self, request):
        return render(request, 'query.html', context={'queries': models.Query.objects.get_search_queries()})

    def post(self, request):
        query = request.POST.get('query')
        if query and not models.Query.objects.is_query_exists(query):
            models.Query.objects.create(query=query)
            search = search_util.Search(query)
            queue.enqueue(search.search)
        return render(request, 'query.html', context={'queries': models.Query.objects.get_search_queries()})


class Result(View):
    def get(self, request, query):
        return render(request, 'result.html', context={'results': models.Result.objects.get_search_results(query)})
