from django.db import models


class ComicBook(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title


