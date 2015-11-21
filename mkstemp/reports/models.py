from django.db import models
from django.contrib.auth.models import User

from mkstemp.utils import TimeStampMixin


class Report(TimeStampMixin):
    text = models.TextField()
    resolved = models.BooleanField(default=False)

    item = models.ForeignKey('items.Item')
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - by {}".format(self.text[:30], self.user.username)
