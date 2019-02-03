from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<pk>\d+)/$', views.mineral_view, name='detail'),
    url(r'random/', views.random_mineral, name='random')
]
