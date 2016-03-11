__author__ = 'javimuu'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                        {'next_page': '/admin/login/'}, name='logout'),
]