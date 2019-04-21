from django.db import models
import datetime


class ToDo_Item(models.Model):
    content = models.TextField() #Details of the to-do item
    datecreated = models.TextField() #Data of to-do item creation
