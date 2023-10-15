from django.db import models


class Person(models.Model):
    DoesNotExist = None
    name = models.CharField('Имя', max_length=80)
    age = models.IntegerField('Возраст')
    address = models.CharField('Адрес', max_length=200)
    work = models.CharField('Работа', max_length=100)

    def __str__(self):
        return self.name
