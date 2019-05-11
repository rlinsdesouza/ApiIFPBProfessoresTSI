from django.db import models

# Create your models here.

class Professor (models.Model) :
    nome = models.CharField(max_length=100, blank=False)
    frasemarcante = models.CharField(max_length=100)
    foto = models.ImageField(
        # upload_to=None,
        # height_field=None,
        # width_field=None,
        # max_length=None,
        null=True,
        # allow_empty_file=False,
        # use_url=True,
        )

    def __str__(self):
        return '%s: %s' % (self.nome, self.frasemarcante)

    class Meta:
        ordering = ('nome',)
  