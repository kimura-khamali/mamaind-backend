# from django.db import models


# class Mother(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     no_of_children = models.IntegerField()
#     date_of_reg = models.DateField()
#     tel_no = models.CharField(max_length=15)
#     marital_status = models.CharField(max_length=20)
#     sub_location = models.CharField(max_length=100)
#     village = models.CharField(max_length=100)


#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

from django.core.exceptions import ValidationError
from django.db import models


class Mother(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    no_of_children = models.PositiveIntegerField()  # Only allows non-negative integers
    date_of_reg = models.DateField(null=True, blank=True)
    tel_no = models.CharField(max_length=15)

    marital_status = models.CharField(max_length=20)
    sub_location = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
