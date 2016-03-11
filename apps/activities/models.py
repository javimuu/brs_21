from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Activity(models.Model):
    TYPE = (
        (1, 'follow'),
        (2, 'comment'),
        (3, 'favorite'),
        (4, 'review'),
        (5, 'read_status')
    )

    type = models.IntegerField()
    target_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'activities'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
