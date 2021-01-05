from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Text')
    date = models.DateTimeField('DateTime')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
