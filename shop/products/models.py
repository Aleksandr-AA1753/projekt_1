from django.db import models

class General(models.Model):
    manufacturer = models.CharField(max_length=100, db_index=True, verbose_name='Производитель')
    model = models.CharField(max_length=100, blank=True, verbose_name='Модель')
    price = models.FloatField(default=0.0, db_index=True, verbose_name='Цена')
    photo = models.ImageField(verbose_name = 'Фотография')
    manual = models.FileField(verbose_name = 'Инструкция', blank=True)
    year_of_release = models.DateField(blank=True, verbose_name='Год выпуска')
    weight = models.FloatField(blank=True, verbose_name='Вес')
    colour = models.CharField(max_length=100, blank=True, verbose_name='Цвет')
    packing_height = models.FloatField(blank=True, verbose_name='Ширина упаковки')
    package_width = models.FloatField(blank=True, verbose_name='Высота упаковки')
    packing_depth = models.FloatField(blank=True, verbose_name='Глубина упаковки')
    packing_volume = models.FloatField(blank=True, verbose_name='Объем упаковки')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return self.manufacturer
    
    class Meta():
        verbose_name='Общие данные'
        verbose_name_plural='Общие данные'