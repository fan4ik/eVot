from django.db import models

class Candidat(models.Model):
    nume = models.CharField(max_length=100)
    echipa = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email

