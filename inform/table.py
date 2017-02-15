# -*- coding: utf-8 -*-

import django_tables2 as tables
from .models import EntDbSpr

from django_tables2.utils import A

class Table_Ent(tables.Table):   # Main table

    npr = tables.LinkColumn('object_detail', args=[A('id_entdbspr')])
    #npr = tables.Column()
    npr.verbose_name = "Название предприятия"

    adr = tables.Column()
    adr.verbose_name = "Адрес предприятия"

    gup=tables.Column()
    gup.verbose_name = "Код предприятия по ГВК"

    oku=tables.Column()
    oku.verbose_name = "УНН предприятия"

    okp = tables.Column()
    okp.verbose_name = "ОКПО предприятия"

    class Meta:
        model = EntDbSpr
        attrs= {"class":"paleblue"}
        fields = ('npr','adr','gup','oku','okp')
        per_page = 15