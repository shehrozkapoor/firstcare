from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# type of users we have in the system will be saved in to the database and we can assign different roles to them

class UserType(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

# custoUser is inherited by the AbstractUser class and adding extra field to it.
class CustomUser(AbstractUser):
    digital_sign = models.FileField(null=True,blank=True)
    suffix = models.CharField(max_length=100,null=True,blank=True)
    userType = models.ForeignKey(UserType,on_delete=models.CASCADE,null=False,blank=False,default=4,db_constraint=False)


#this will create a token when we will create a new user from anywhere wheather it will be admin panel or API

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
