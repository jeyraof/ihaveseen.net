from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    ACTIVITY_MODELS = ['Profile', 'Work', 'Episode', 'Record', ]
    ACTIVITY_ACTIONS = ['Create', 'Update', 'Delete', ]

    user = models.ForeignKey(User)
    model = models.CharField(choices={j: j for j in ACTIVITY_MODELS}.items(), max_length=20)
    tid = models.IntegerField(blank=False, null=False)
    action = models.CharField(choices={j: j for j in ACTIVITY_ACTIONS}.items(), max_length=10)
    old_value = models.CharField(blank=True, max_length=255, null=True)
    new_value = models.CharField(blank=True, max_length=255, null=True)
    extra = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity'
        ordering = ['-created_at', ]
