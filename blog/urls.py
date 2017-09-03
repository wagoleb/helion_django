from blog import urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postsList, name='postList'),
    url(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.postDetail, name='postDetail')
]
