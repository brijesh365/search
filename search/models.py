from django.db import models
from django.utils.translation import ugettext_lazy as _
from picklefield import PickledObjectField

from search.constants import IN_PROGRESS, STATUS_CHOICES
from search.manager import QueryManager, ResultManager
from utils import models as base_model


class Query(base_model.BaseModel):
    query = models.CharField(max_length=256, db_index=True, unique=True)
    status = models.CharField(choices=STATUS_CHOICES, default=IN_PROGRESS, max_length=30)

    objects = QueryManager()

    class Meta:
        verbose_name = _('search')
        verbose_name_plural = _('searches')


class Result(base_model.BaseModel):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    engine = models.CharField(max_length=100)
    result = PickledObjectField()

    objects = ResultManager()

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('results')
