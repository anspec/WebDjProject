from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField(verbose_name='Название',max_length=100)
    description = models.CharField(verbose_name='Кратко',max_length=250)
    usr_name = models.CharField(verbose_name='Опубликовал',max_length=100)
    txt = models.TextField(verbose_name='Новость')
    dat_pub = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

