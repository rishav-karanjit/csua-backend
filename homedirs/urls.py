from django.conf.urls import url
from homedirs import views

urlpatterns = [
    url(r'(?P<username>[a-zA-Z0-9]+)/(?P<path>.*)$', views.serve),
]
