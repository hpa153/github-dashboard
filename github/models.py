from unicodedata import name
from django.db import models

from account.models import Account

# Create your models here.
class Chart(models.Model):
  user_id = models.ForeignKey(
    Account,
    on_delete=models.CASCADE,
  )
  name = models.CharField(max_length=64, default="")
  repo = models.CharField(max_length=64, default="")
  path = models.CharField(max_length=150, default="")
  chart_style = models.CharField(max_length=25, default="DefaultStyle")
  chart_type = models.CharField(max_length=5, default="bar")

  def get_name(self):
    return self.name

  def get_repo(self):
    return self.repo

  def get_path(self):
    return self.path

  def get_chart_style(self):
    return self.chart_style

  def get_chart_type(self):
    return self.chart_type
