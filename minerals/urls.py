from django.conf.urls import url

from . import views

app_name = 'minerals'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<pk>\d+)/$', views.mineral_view, name='detail'),
    url(r'random/', views.random_mineral, name='random'),
    url(r'^initial/(?P<initial>\w)',
        views.list_by_initial, name="list_by_initial"),
    url(r'search/$', views.search, name='search'),
    url(r'filter/$', views.filter_by, name='filter_by'),
]
