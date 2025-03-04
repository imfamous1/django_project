from django.db import models

# Create your models here.

class TelegramUsers(models.Model):
    user_id = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return f'\nUSER_ID:{self.user_id}\nUSERNAME:{self.username}\nWALLET:{self.wallet}\n'