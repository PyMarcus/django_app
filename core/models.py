from django.db import models


class Product(models.Model):
    name: str = models.CharField('name', max_length=100)
    price: float = models.DecimalField('price', decimal_places=2, max_digits=9)
    store: int = models.IntegerField("Length")

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name: str = models.CharField('name', max_length=100)
    age: int = models.IntegerField('age')
    email: str = models.CharField('email', max_length=100)

    def __str__(self) -> str:
        return self.name
