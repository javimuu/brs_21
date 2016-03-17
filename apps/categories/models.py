from django.db import models


class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'categories'

