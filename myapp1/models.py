from django.db import models

# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=40)
    lead = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class TelegramUsers(models.Model):
    user_id = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    wallet = models.IntegerField(default=0)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'{self.username}'




