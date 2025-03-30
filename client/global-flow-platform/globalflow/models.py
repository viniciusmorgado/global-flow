from django.utils import timezone
from django.db import models
import uuid

class Base(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Sale(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return str(self.item)

class BusinessRole(Base):
    name = models.CharField(max_length=250)

class TaxRegime(Base):
    name = models.CharField(max_length=250)

class Honorary(Base):
    name = models.CharField(max_length=250)

class MinimumFee(Base):
    name = models.CharField(max_length=250)

class SampleFee(Base):
    name = models.CharField(max_length=250)

class Dispatcher(Base):
    name = models.CharField(max_length=250)

class Insurance(Base):
    name = models.CharField(max_length=250)

class Radar(Base):
    name = models.CharField(max_length=100)

# class Business(Base):
#     business_name = models.CharField(max_length=250)
#     business_role = 