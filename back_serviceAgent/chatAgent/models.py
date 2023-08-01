from django.db import models
from companyAdmin.models import CompanyUser
from django.contrib.auth.models import User


class ClientUser(models.Model):
    clientUser_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='None')
    last_name = models.CharField(max_length=100, default='None')
    email = models.EmailField(default='None')
    phone_number = models.IntegerField(default=0) 
    company = models.ForeignKey(CompanyUser, on_delete=models.CASCADE, default=1)
    current_conversation = models.ForeignKey('Conversation', on_delete=models.SET_NULL, null=True, blank=True)

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    clientUser = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('finished', 'Finished'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Conversation {self.id} - {self.clientUser.first_name}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    SENDER_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]
    sender = models.CharField(max_length=9, choices=SENDER_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text} ({self.timestamp})"

    class Meta:
        ordering = ['timestamp']


