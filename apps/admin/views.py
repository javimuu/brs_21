from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import (
    reverse_lazy,
    reverse,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.generic import (
    FormView,
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
)

from .form import AdminAuthForm

from apps.categories.models import Category

from apps.categories.form import (
    CategoryForm,
)

LOGIN_PAGE = reverse_lazy("admin:login")


class AdminRequiredMixin(object):
    """
    View mixin for staff app. Required admin group.
    """

    @method_decorator(login_required(login_url=LOGIN_PAGE))
    def dispatch(self,request, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


# Section: Auth

class IndexView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class LoginView(FormView):
    """
    Admin log in view
    """

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

# End Section Auth


# Section: Categories

class CategoryView(AdminRequiredMixin, ListView):
    """
    View list categories
    """

    model = Category
    context_object_name = 'categories'
    template_name = 'admin/categories/index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        info = {
            'title': 'Book Review System - List',
        }
        context['info'] = info
        return context


class CategoryCreateView(AdminRequiredMixin, CreateView):
    """
    Create a new category
    """

    model = Category
    form_class = CategoryForm
    template_name = 'admin/categories/new.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create a Category | Book Review System ',
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:category')


class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    """
    Create a new category
    """

    model = Category
    form_class = CategoryForm
    template_name = 'admin/categories/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Category | Book Review System',
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:category')

# End Section Categories
