# -*- coding: utf-8 -*-

import django_filters
from .models import EntDbSpr
from django_filters.filters import CharFilter



EMPTY_CHOICE = ('', '---------'), # Don't forget the trailing comma


class EntDbFilter(django_filters.FilterSet):

    gup = django_filters.CharFilter(label='Код по ГВК (ввод в строке)',lookup_type='contains')
    npr = django_filters.CharFilter(label='Название субъекта хозяйствования (ввод в строке)', lookup_type='contains')
    oku = django_filters.CharFilter(label='УНН (ввод в строке)', lookup_type='contains')

    class Meta:
        model = EntDbSpr
        fields = ['gup','oku','npr']



    def __init__(self, *args, **kwargs):
        super(EntDbFilter, self).__init__(*args, **kwargs)
