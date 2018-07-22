from django.db import models

# Create your models here.

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
