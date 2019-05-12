from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Professor (models.Model) :
    nome = models.CharField(max_length=100, blank=False)
    frasemarcante = models.CharField(max_length=100)
    foto = CloudinaryField(
        'foto',
        null=True
    )

    def __str__(self):
        return '{} : {}'.format(self.nome, self.frasemarcante)

    class Meta:
        ordering = ('nome',)
