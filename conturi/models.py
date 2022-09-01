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

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return '%d %d %s %s %s %s %s' % (self.pk, self.user.id, self.user.first_name, self.user.last_name, self.user.username, self.user.email, self.statut_UserAprobat)

    def isApproved(self):
        return self.statut_UserAprobat

    def getApproved(self):
        self.statut_UserAprobat = True