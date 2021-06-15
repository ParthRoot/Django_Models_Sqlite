from django.db import models
import uuid

# Create your models here.
class register_form(models.Model):
    add_date = models.DateField(max_length=10, primary_key=True, default=uuid.uuid1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.TextField(max_length=10)
    course = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    