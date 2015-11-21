from django.db import models
from django.contrib.auth.models import User

from mkstemp.utils import TimeStampMixin


class Report(TimeStampMixin):
    text = models.TextField()
    resolved = models.BooleanField(default=False)
    resolution = models.TextField(blank=True)

    item = models.ForeignKey('items.Item')
    user = models.ForeignKey(User, related_name='reports')
    resolved_by = models.ForeignKey(
        User, blank=True, null=True, related_name='resolved_reports')

    def __str__(self):
        return "{} - by {}".format(self.text[:30], self.user.username)
