__author__ = 'javimuu'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                        {'next_page': '/admin/login/'}, name='logout'),
    url(r'^categories/$', views.CategoryView.as_view(), name='category'),
    url(r'^categories/new/$', views.CategoryCreateView.as_view(), name='new_category'),
    url(r'^categories/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(),
                        name='edit_category'),
]
