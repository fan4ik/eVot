from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gen = models.CharField(max_length=1, default='0')
    data_nastere = models.DateField()
    localitate = models.CharField(max_length=100)
    adresa = models.CharField(max_length=150)
    nr_telefon = PhoneNumberField()
    token = models.CharField(max_length=100)

    document_fata = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    document_verso = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    statut_UserAprobat = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.user.last_name, self.user.first_name)

    def isApproved(self):
        return self.statut_UserAprobat

    def getApproved(self):
        self.approvalStatus = True