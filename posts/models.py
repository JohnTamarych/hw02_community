from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='post',
        blank=True,
        null=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        if self.group is not None:
            responce = f'У {self.author} новый пост в {self.group}'
        else:
            responce = f'У {self.author} новый пост'
        return responce
