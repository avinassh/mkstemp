from django.db import models
from django.contrib.auth.models import User

from mkstemp.utils import TimeStampMixin


class Item(TimeStampMixin):
    title = models.CharField(max_length=300)
    text = models.TextField()
    url = models.URLField()
    item_type = models.IntegerField()
    locked = models.BooleanField()

    parent = models.ForeignKey('self', null=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "<{} - {}>".format(self.id, self.title[:30])
