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
    name = models.DecimalField(max_digits=6, decimal_places=2)

class SampleFee(Base):
    name = models.DecimalField(max_digits=6, decimal_places=2)

class Dispatcher(Base):
    name = models.CharField(max_length=250)

class Insurance(Base):
    name = models.CharField(max_length=250)

class Radar(Base):
    name = models.CharField(max_length=250)

class Business(Base):
    business_name = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=250)
    business_contact = models.CharField(max_length=250)
    business_role = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    mobile_phone = models.CharField(max_length=250)
    simulation_cost_email = models.CharField(max_length=250)
    business_email = models.CharField(max_length=250)
    tax_regime = models.ForeignKey(TaxRegime, null=True, on_delete=models.CASCADE)
    honorary = models.ForeignKey(Honorary, null=True, on_delete=models.CASCADE)
    minimum_fee = models.ForeignKey(MinimumFee, null=True, on_delete=models.CASCADE)
    sample_fee = models.ForeignKey(SampleFee, null=True, on_delete=models.CASCADE)
    dispatcher = models.ForeignKey(Dispatcher, null=True, on_delete=models.CASCADE)
    honorary_value = models.CharField(max_length=250)
    sdas = models.CharField(max_length=250)
    insurance = models.ForeignKey(Insurance, null=True, on_delete=models.CASCADE)
    radar = models.ForeignKey(Radar, null=True, on_delete=models.CASCADE)
    validity_attorney = models.CharField(max_length=250)
    exchange_closing = models.CharField(max_length=250)
    exchange_where = models.CharField(max_length=250)
