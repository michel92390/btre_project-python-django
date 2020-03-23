from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='listings'),
    url(r'^(?P<listing_id>[0-9]+)/$',views.listing,name='listing'),
    #url(r'^listing/', views.listing, name='listing'),
    url(r'^search/', views.search, name='search'),
]


