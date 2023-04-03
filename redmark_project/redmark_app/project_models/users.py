from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    taken = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    answer = models.ManyToManyField('Answer', related_name='user_to_ans')

    def __str__(self):
        return self.user
