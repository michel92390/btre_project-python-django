from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/',views.register,name='register'),
    #url(r'^listing/', views.listing, name='listing'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
