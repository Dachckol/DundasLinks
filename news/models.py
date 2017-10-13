from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
