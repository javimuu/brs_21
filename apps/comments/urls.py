from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.create_comment, name='new'),
    url(r'^emoticons/$', views.emoticons, name='emotions'),
    url(r'^(?P<comment_id>[0-9]+)/edit/$', views.edit_comment, name='edit'),
    url(r'^delete/$', views.delete_comment, name='delete'),
]


