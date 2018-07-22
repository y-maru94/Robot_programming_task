from django.db import models

class Worker(models.Model):
    # 人
    person = models.ForeignKey('Person')
