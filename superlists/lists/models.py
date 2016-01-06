from __future__ import unicode_literals
from django.db import models

#models.Model has all the saving fuctionallity we need
#for our test_saving_and_retrieving_items class
class Item(models.Model):
    text = models.TextField(default = '')
