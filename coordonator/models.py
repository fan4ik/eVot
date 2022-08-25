from django.db import models

class Alegere(models.Model):
    status = models.BooleanField(default=False)

    def __bool__(self):
        return self.status
