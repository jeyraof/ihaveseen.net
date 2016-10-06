from django.contrib.auth.models import User
from django.db import models
from work.models import Episode, Work


class Record(models.Model):
    RECORD_COMPLETE = 'Complete'
    RECORD_DOING = 'Doing'
    RECORD_STATUS = [RECORD_COMPLETE, RECORD_DOING]

    user = models.ForeignKey(User, blank=False, db_index=True, on_delete=models.CASCADE, related_name='records')
    work = models.ForeignKey(Work, blank=False, db_index=True, on_delete=models.CASCADE, related_name='records')
    episode = models.ForeignKey(Episode, blank=True, on_delete=models.CASCADE)
    status = models.CharField(blank=False, choices={j: j for j in RECORD_STATUS}.items(),
                              default=RECORD_DOING, max_length=10)

    class Meta:
        db_table = 'record'
        index_together = [
            ('user', 'work', 'episode'),
            ('user', 'work'),
            ('work', 'episode'),
        ]
        unique_together = ('user', 'work', 'episode', )
