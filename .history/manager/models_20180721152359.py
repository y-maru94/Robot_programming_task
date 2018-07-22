from django.db import models

class Worker(models.Model):

    # 人
    person = models.ForeignKey('Person')
    # 着任時期
    joined_at = models.DateTimeField()
    # やめた時期
    quited_at = models.DateTimeField(null=True, blank=True)
    # 担当上司
    manager = models.ForeignKey('Manager')
