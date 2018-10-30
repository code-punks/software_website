from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# class CustomUser(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True,null=True)
#     location = models.CharField(max_length=30, blank=True,null=True)
#     birth_date = models.DateField(null=True, blank=True)
#     phone_number = models.IntegerField(blank=True,null=True)
#     rfid = models.CharField(max_length=100,blank=True,null=True)
#     REQUIRED_FIELDS = ['bio','location','birth_date','phone_number']
#     def __str__(self):
#     	return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    rfid = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()