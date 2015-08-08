from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    nominator = models.ForeignKey(User, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    show_date = models.DateTimeField(null=True, blank=True)
    showing = models.BooleanField(default=False)
    shown = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.vote_count = self.votes.all().count()
        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{0} [{1}]'.format(self.title, self.release_year)
