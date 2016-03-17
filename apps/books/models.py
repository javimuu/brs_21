from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from apps.categories.models import Category
from apps.core.view import upload_to_imgur


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    publish_date = models.DateTimeField()
    description = models.TextField(blank=True, default='')
    price = models.FloatField(null=False, blank=False, default=0.0)
    # cover = models.ImageField(upload_to=upload_to_imgur, max_length=255, default='', blank=False)
    categories = models.ManyToManyField(Category, through='BookCategory')
    class Meta:
        db_table = 'books'



class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_category'
        auto_created = True


class UserBook(models.Model):
    READING = 1
    READ = 2
    READING_STATUS = (
            (READING, 'Reading'),
            (READ, 'Read'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.IntegerField(choices=READING_STATUS, default=READING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_book'

