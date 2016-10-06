from datetime import datetime
from django.db import models
from django.urls import reverse


class Work(models.Model):
    # types
    TYPE_COMIC = 'comic'
    TYPE_DRAMA = 'drama'
    TYPE_NOVEL = 'novel'
    TYPE_MOVIE = 'movie'
    CHOICE_DICT = {TYPE_COMIC: '만화',
                   TYPE_DRAMA: '드라마',
                   TYPE_NOVEL: '소설',
                   TYPE_MOVIE: '영화'}

    # columns
    type = models.CharField(choices=CHOICE_DICT.items(), max_length=10)
    title = models.CharField(max_length=255)
    shorten_url = models.CharField(max_length=50, null=True)
    complete = models.BooleanField(default=False)
    debut_at = models.DateField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'work'
        ordering = ('-created_at', )

    def __str__(self):
        return '[{type}] {title}'.format(type=self.get_type_display(), title=self.title)

    def get_absolute_url(self):
        return reverse('', args=[str(self.type), str(self.shorten_url)])

    def publish(self):
        self.published_at = datetime.utcnow()
        self.save()


class Episode(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='episodes', related_query_name='episode')
    eid = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    published_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'episode'
        ordering = ('-published_at', '-eid', )
