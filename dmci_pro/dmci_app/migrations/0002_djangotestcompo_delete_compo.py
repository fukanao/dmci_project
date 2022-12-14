# Generated by Django 4.0.1 on 2022-11-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmci_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoTestCompo',
            fields=[
                ('id_num', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_text', models.TextField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(blank=True, null=True)),
                ('updated_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_test_compo',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='compo',
        ),
    ]
