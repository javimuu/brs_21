from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
# from .models import *
from .forms import *


class SignupView(FormView):
    model = User
    form_class = SignupViewForm
    success_url = '/signin'
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

    def get_success_url(self, user=None):
        return super(SignupView, self).get_success_url()
