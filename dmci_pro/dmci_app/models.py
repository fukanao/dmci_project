from django.db import models

# Create your models here.

class DjangoTestMain(models.Model):
    id = models.AutoField(primary_key=True)
    quatation_meta_id = models.CharField(max_length=100)
    quatation_subject = models.TextField(blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    reserve_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quatation_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    updated_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_test_main'


class DjangoTestCompo(models.Model):
    id_num = models.AutoField(primary_key=True)
    quatation_meta_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_text = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    updated_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_test_compo'

