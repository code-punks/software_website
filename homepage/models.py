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
    def __str__(self):
        return self.user.username

class Bill(models.Model):
    rfid = models.OneToOneField(User)
    month = models.IntegerField( blank = True)
    monthly_amount = models.IntegerField( blank = True)
    def __str__(self):
        return self.rfid

class Payment(models.Model):
    date = models.DateField(blank = True)
    payment_month = models.IntegerField(blank = True)
    amount_paid = models.IntegerField( blank = True)
    rfid = models.OneToOneField(Bill, on_delete = models.CASCADE)

class Balance(models.Model):
    rfid = models.OneToOneField(Payment, on_delete = models.CASCADE)
    payment_balance = models.IntegerField( blank = True)
    month = models.IntegerField( blank = True)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()