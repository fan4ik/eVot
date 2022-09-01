from django.db import models

class Alegere(models.Model):
    status_Alegere = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Alegeri"

    def __bool__(self):
        return self.status_Alegere
