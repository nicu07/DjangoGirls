# Create your models here.
from django.db import models  #en algun lugar hay django.db, de ese yo quiero traer el models
from django.utils import timezone #Estoy importando fechas

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now) #Coge la fecha actual
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #Controlamos
        self.published_date = timezone.now() #Coge la fecha actual
        self.save()

    def __str__(self): #Ya existe, se esta sobreescribiendo. Me va a devolver algo.
        return self.title
