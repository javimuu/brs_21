from django.views.generic import DetailView

from apps.books.models import Book
# Create your views here.


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

