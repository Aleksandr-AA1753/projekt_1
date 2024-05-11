from django.db import models

from references.models import ReferencesManufacturer

class General(models.Model):
    model = models.CharField(max_length=100, blank=True, verbose_name='Модель')
    price = models.FloatField(default=0.0, db_index=True, verbose_name='Цена')
    photo = models.ImageField(verbose_name = 'Фотография')
    manual = models.FileField(verbose_name = 'Инструкция', blank=True)
    year_of_release = models.DateField(blank=True, verbose_name='Год выпуска')
    weight = models.FloatField(blank=True, verbose_name='Вес')
    packing_height = models.FloatField(blank=True, verbose_name='Ширина упаковки')
    package_width = models.FloatField(blank=True, verbose_name='Высота упаковки')
    packing_depth = models.FloatField(blank=True, verbose_name='Глубина упаковки')
    packing_volume = models.FloatField(blank=True, verbose_name='Объем упаковки')
    description = models.TextField(blank=True, verbose_name='описание')
    #ref_gen_id1 = models.ForeignKey('ReferencesManufacturer', on_delete=models.PROTECT)
    #ref_gen_id2 = models.ForeignKey('ReferencesColour', on_delete=models.PROTECT)
    #ref_gen_id3= models.ForeignKey('ReferencesProduct_type', on_delete=models.PROTECT)

    def __str__(self):
        return self.model
    
    class Meta():
        verbose_name='Общие данные'
        verbose_name_plural='Общие данные'


class Fridge(models.Model):
    embedded = models.BooleanField(default=False, verbose_name='Встраиваемый')
    number_of_doors = models.IntegerField(blank=True, verbose_name='Количество дверей')
    height = models.FloatField(blank=True, verbose_name='Ширина')
    width = models.FloatField(blank=True, verbose_name='Высота')
    depth = models.FloatField(blank=True, verbose_name='Глубина')
    #ref_fri_id1 = models.ForeignKey('ReferencesManufacturer', on_delete=models.PROTECT)
    #ref_fri_id2 = models.ForeignKey('ReferencesColour', on_delete=models.PROTECT)
    #ref_fri_id3= models.ForeignKey('ReferencesProduct_type', on_delete=models.PROTECT)

    def __str__(self):
        return self.embedded
    
    class Meta():
        verbose_name='Холодильник'
        verbose_name_plural='Холодильники'