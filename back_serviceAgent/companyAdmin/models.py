from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.dispatch import receiver
from django.db.models.signals import post_save

class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    CompanyUser.objects.get_or_create(user=instance)

class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    endpoint = models.CharField(max_length=100)
    company = models.ForeignKey(CompanyUser, on_delete=models.CASCADE, related_name='functions')
    parameters = JSONField()

    def __str__(self):
        return self.name
