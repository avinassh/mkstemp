from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from mkstemp.utils import TimeStampMixin


class Item(TimeStampMixin):
    title = models.CharField(max_length=300, blank=True)
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)
    locked = models.BooleanField(default=False)

    parent = models.ForeignKey('self', null=True, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "<{} - {}>".format(self.id, self.title[:30])

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.id})

    def get_comments(self):
        return self.item_set.order_by('created_on')

    class Meta:
        ordering = ['-created_on']


class Report(TimeStampMixin):
    text = models.TextField()
    resolved = models.BooleanField(default=False)

    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - by {}".format(self.text[:30], self.user.username)
