from django.db import models
from django.contrib.auth.models import User
from apps.reviews.models import Review
# Create your models here.


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'

