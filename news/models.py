from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(blank=True, null=True)
    text = models.TextField()


    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return str(self.text)[0:15]

    