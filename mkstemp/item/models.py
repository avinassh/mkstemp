from django.db import models
from django.contrib.auth.models import User

from mkstemp.utils import TimeStampMixin


class Item(TimeStampMixin):
    title = models.CharField(max_length=300, blank=True)
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)
    item_type = models.IntegerField()
    locked = models.BooleanField(default=False)
    slug = models.SlugField(max_length=6)

    parent = models.ForeignKey('self', null=True, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "<{} - {}>".format(self.id, self.title[:30])

    class Meta:
        ordering = ['-created_on']


class Report(TimeStampMixin):
    text = models.TextField()
    resolved = models.BooleanField(default=False)

    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - by {}".format(self.text[:30], self.user.username)
