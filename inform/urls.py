from django.conf.urls import url,include
from inform.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^input/', input_page),
    url(r'^initial/',initial_page),
    url(r'ent/(\d+)/', ReportTableViewDetail.as_view(), name='object_detail'),
    url(r'^find/', ReportFindTable.as_view(), name='test_find'),
    url(r'^result/', ReportFindResult.as_view(), name='test_table'),
    url(r'^page1/', part1_view),
    url(r'^page2/', part2_view),
    url(r'^page3/', part3_view),
    url(r'^page4/', part4_view),
    url(r'^api/?$', Clients.as_view()),
    url(r'^api/(?P<part1_id>[0-9]+)/?$', Clients.as_view()),
    ]