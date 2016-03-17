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
    DetailView,
    DeleteView,
)

from .form import AdminAuthForm

from apps.categories.models import Category
from apps.categories.form import (
    CategoryForm,
    BookCategoryForm
)

from apps.books.models import (
    Book,
    BookCategory,
)
from apps.books.form import  BookForm

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


class CategoryDetailView(AdminRequiredMixin, DetailView):
    """
    View list categories
    """

    model = Category
    context_object_name = 'category'
    template_name = 'admin/categories/detail.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        info = {
            'title': 'Detail category | Book Review System',
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


# Section Manage Book

class BookView(AdminRequiredMixin, ListView):
    """
    View list categories
    """

    model = Book
    context_object_name = 'books'
    template_name = 'admin/books/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BookView, self).get_context_data(**kwargs)
        info = {
            'title': 'Book Review System - List',
        }
        context['info'] = info
        return context


class BookCreateView(AdminRequiredMixin, CreateView):
    """
    Create a new book
    """
    model = Book
    form_class = BookForm
    template_name = 'admin/books/new.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create a new Book | Book Review System ',
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:book')


class BookUpdateView(AdminRequiredMixin, UpdateView):
    """
    Edit a book
    """

    model = Book
    form_class = BookForm
    template_name = 'admin/books/edit.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update a book | Book Review System',
        }
        context['info'] = info
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('admin:book')


class BookDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for BookDeleteView"""
    model = Book

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:book')

# End Section Manage Book
