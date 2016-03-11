__author__ = 'javimuu'

from django.contrib.admin.forms import AdminAuthenticationForm

class AdminAuthForm(AdminAuthenticationForm):

    class Meta:
        fields = ['username','password']
