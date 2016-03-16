from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    followers = models.ManyToManyField('self', through='Follows',
        through_fields=('followed', 'follower'),
        related_name='following', symmetrical=False)
    avatar = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'user_profile'


class Follows(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follower')
    followed = models.ForeignKey(UserProfile, related_name='followed')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'follows'
