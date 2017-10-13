from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contentType = models.ForeignKey(Type)
    content = models.TextField(max_length=600)
    answered = models.BooleanField(default=False)

    def __unicode__(self):
        return self.contentType.name

    def __str__(self):
        return self.contentType.name
