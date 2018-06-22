from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name="Название")
    order = models.PositiveIntegerField(db_index=True, verbose_name="Порядковый номер", default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "категория"
        verbose_name_plural = "категории"
