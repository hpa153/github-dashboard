from unicodedata import name
from django.db import models

from account.models import Account

# Create your models here.
class Chart(models.Model):
  user = models.ForeignKey(
    Account,
    on_delete=models.CASCADE,
  )
  name = models.CharField(max_length=64, default="")
  chart = models.TextField()

  def get_name(self):
    return self.name

  def get_chart(self):
    return self.chart
