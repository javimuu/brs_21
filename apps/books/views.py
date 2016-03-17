from django.core.urlresolvers import (
    reverse_lazy,
    reverse,
)
from django.utils.decorators import method_decorator
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
)
from apps.core.view import *
from apps.books.models import Book


# Section Site Index

class SiteIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(SiteIndexView, self).get_context_data(**kwargs)
        context['title'] = "Home page"
        context['books'] = Book.objects.all()
        return context

# End section Site Index

class DetailBookView(DetailView):
    template_name = 'books/detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(DetailBookView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.title
            }
        }
        context.update(info)
        return context

