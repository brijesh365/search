from django.urls import path

from search import views

urlpatterns = [
    path('query/', views.Query.as_view(), name='query'),
    path('result/<str:query>/', views.Result.as_view(), name='result'),
]
