from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape
from apps.reviews.models import Review
from .icons import ICONS
# Create your models here.


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

    @property
    def parse_comment(self):
        comment = escape(self.comment)
        for key, value in ICONS.items():
            comment = comment.replace(key, r'<img src="'+value+'" alt="'+key+'"></img>')
        return comment

