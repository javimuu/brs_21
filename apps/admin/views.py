from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from django.contrib.admin.forms import AdminAuthenticationForm
from django.views.generic import (
        FormView, View, CreateView, DetailView,
        UpdateView, DeleteView, TemplateView, ListView,
)

from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views import generic



LOGIN_PAGE = reverse_lazy("login")


class AdminRequiredMixin(object):
    """
    View mixin for staff app. Required admin group.
    """

    @method_decorator(login_required(login_url=LOGIN_PAGE))
    def dispatch(self,request, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


class LoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)
