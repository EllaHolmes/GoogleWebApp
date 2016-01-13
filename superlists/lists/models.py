from __future__ import unicode_literals
from django.db import models

#models.Model has all the saving fuctionallity we need
#for our test_saving_and_retrieving_items class
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default = '')
    list = models.ForeignKey(List, default=None)
    is_done = models.BooleanField(default=False)
