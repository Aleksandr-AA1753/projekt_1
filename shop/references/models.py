from django.db import models


class ReferencesManufacturer(models.Model):
    manufacturer = models.CharField(max_length=100, default="unknown", blank=True, 
        unique=True, null=True, db_index=True, verbose_name='Производитель')
    
    def __str__(self):
        return self.manufacturer
    
    class Meta():
        verbose_name='Справочник производителей'
        verbose_name_plural='Справочник производителей'


class ReferencesColour(models.Model):
    colour = models.CharField(max_length=100, default="unknown", unique=True, null=True, 
        blank=True, verbose_name='Цвет')
    
    def __str__(self):
        return self.colour
    
    class Meta():
        verbose_name='Справочник цвета'
        verbose_name_plural='Справочники цветов'

class ReferencesProduct_type(models.Model):
    product_type = models.CharField(max_length=100, default="unknown", unique=True, 
        blank=True, db_index=True, null=True, verbose_name='Категория товара')

    def __str__(self):
        return self.product_type
    
    class Meta():
        verbose_name='Справочник категорий товаров'
        verbose_name_plural='Справочники категорий товаров'
