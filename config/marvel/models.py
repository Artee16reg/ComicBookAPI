from django.db import models


class ComicBook(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комикс'
        verbose_name_plural = 'Комиксы'
