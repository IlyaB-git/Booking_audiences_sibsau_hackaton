from tabnanny import verbose
from django.db import models

class Corpus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Копрус'
        verbose_name_plural = 'Корпуса'





class Auditor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер')
    places = models.PositiveIntegerField(default=0, verbose_name='Мест')
    tables = models.PositiveIntegerField(default=0, verbose_name='Столов')
    microphones = models.BooleanField(default=False, verbose_name='Микрофон')
    speakers = models.BooleanField(default=False, verbose_name='Колонки')
    computers = models.PositiveIntegerField(default=0, verbose_name='Компьютеры')
    proektor = models.BooleanField(default=False, verbose_name='Проектор')
    interactiveBoard = models.BooleanField(default=False, verbose_name='Интер. доска')
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE, verbose_name='Корпус')
    user = models.CharField(max_length=50, verbose_name='Пользователь', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'

class Bron(models.Model):
    user = models.CharField(max_length=50, verbose_name='Пользователь', blank=True, null=True)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE, blank=True, verbose_name='Аудитория')
    date = models.DateField(verbose_name='Дата')
    allowed = models.BooleanField(default=False, verbose_name='Одобрена')
    start_time = models.PositiveSmallIntegerField(verbose_name='начало')
    end_time = models.PositiveSmallIntegerField(verbose_name='конец')
    comment = models.TextField(max_length=50, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        # ordering = ['-date']

    def __str__(self):
        return self.user
    




