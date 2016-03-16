from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.create_review, name='new'),
    url(r'^(?P<review_id>[0-9]+)/edit/$', views.edit_review, name='edit'),
    url(r'^(?P<book_id>[0-9]+)/view/$', views.view_review, name='view'),
    url(r'^delete/$', views.delete_review, name='delete'),
]

