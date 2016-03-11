from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import (
        FormView,
        TemplateView,
)

from .form import AdminAuthForm

LOGIN_PAGE = reverse_lazy("admin:login")


class AdminRequiredMixin(object):
    """
    View mixin for staff app. Required admin group.
    """

    @method_decorator(login_required(login_url=LOGIN_PAGE))
    def dispatch(self,request, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)

class IndexView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class LoginView(FormView):
    form_class = AdminAuthForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:index')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)
