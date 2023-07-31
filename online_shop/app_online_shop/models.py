from django.db import models

# Create your models here.

# Создаём класс с описанием структуры будующей таблицы (наследуемся о класса Model)
class OnlineShop(models.Model):
        # Заголовок
        # CharField класс, обозначающий символьное поле (набор символов), для небольших текстов
        title = models.CharField('Заголовок', max_length=128)
        # описание объявления
        # TextField класс, обозначающий строковое поле больших размеров
        description = models.TextField('Описание')
        # цена
        # DecimalField дробное число с фиксированной точностью (похоже на float в Python)
        # max_digits максимальное кол-во цифр в числе
        # decimal_places максимальное кол-во знаков после запятой
        price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
        # возможность торговаться
        # BooleanField логический тип данных (истина или ложь)
        auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
        # дата размещения объявления
        # auto_now_add=True сразу получаем дату в момент создания объявления
        creation_time = models.DateTimeField(auto_now_add=True)
        # дата обновления объявления
        # auto_now=True получаем дату в момент обновления объявления
        update_time = models.DateTimeField(auto_now=True)
        def __str__(self):
              return f"OnlineShop(id={self.id}, title={self.title}, price={self.price})"
        class Meta:
            db_table = 'advertisements'
