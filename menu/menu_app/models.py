from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка', max_length=256)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
