from django.db import models
from django.contrib.auth.models import User

from mkstemp.utils import TimeStampMixin


class Item(TimeStampMixin):
    title = models.CharField(max_length=300, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    item_type = models.IntegerField()
    locked = models.BooleanField()
    slug = models.SlugField(max_length=6)

    parent = models.ForeignKey('self', null=True, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "<{} - {}>".format(self.id, self.title[:30])


class Report(TimeStampMixin):
    text = models.TextField()
    resolved = models.BooleanField(default=False)

    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - by {}".format(self.text[:30], self.user.username)
