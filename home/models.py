from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Home(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    desc_data = models.CharField(max_length=300)

    def __str__(self):
        return self.first_name