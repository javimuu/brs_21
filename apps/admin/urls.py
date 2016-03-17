from django.conf.urls import url
from . import views

urlpatterns = [

    ### Auth

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/login/'}, name='logout'),

    ### Categories

    url(r'^categories/$', views.CategoryView.as_view(), name='category'),
    url(r'^categories/detail/(?P<pk>[0-9]+)/$', views.CategoryDetailView.as_view(), name='detail_category'),
    url(r'^categories/new/$', views.CategoryCreateView.as_view(), name='new_category'),
    url(r'^categories/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(), name='edit_category'),

    ### Books

    url(r'^books/$', views.BookView.as_view(), name='book'),
    url(r'^books/new/$', views.BookCreateView.as_view(), name='new_book'),
    url(r'^books/update/(?P<pk>[0-9]+)/$', views.BookUpdateView.as_view(), name='edit_book'),
    url(r'^books/delete/(?P<pk>[0-9]+)/$', views.BookDeleteView.as_view(), name='delete_book'),
]
