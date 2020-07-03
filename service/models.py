from django.db import models
from users.models import UserProfile


class Service(models.Model):
    name_service = models.CharField('Nombre Servicio', max_length=50)
    description_service = models.TextField('Descripción del servicio', max_length=600)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_service
