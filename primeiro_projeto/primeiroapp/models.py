from django.db import models

# Create your models here.

# Cada model é como se fosse uma entidade no nosso db e cada atributo é uma coluna
class MenuItem(models.Model):
    name = models.CharField(max_length=255) # usamos isso para definir o que o atributo aceita e o tamanho máximo
    price = models.IntegerField()
    #Agora precisamos fazer as migrations

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True) #Vai pegar automaticamente a data
    comment = models.CharField(max_length=1000)
