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

class Entry(models.Model):
    user = models.OneToOneField(User)
    entry_time = models.DateTimeField(blank = True,null = True)
    exit_time = models.DateTimeField(blank = True)
    time = models.IntegerField(blank = True)
    vehicle_type = models.IntegerField(blank = True,null = True)
    amount = models.IntegerField(blank = True)

    def update_time(self):
        return self.exit_time - self.entry_time

    def calculate_amount(self):
        if(self.time != None and self.vehicle_type != None):
            if(self.vehicle_type == 1):
                return time * 40 
            else:
                return time * 30

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()