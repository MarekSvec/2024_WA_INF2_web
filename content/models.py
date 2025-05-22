from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=600)
    order = models.IntegerField(default=0)


    def __str__(self):
        return self.title[:20]