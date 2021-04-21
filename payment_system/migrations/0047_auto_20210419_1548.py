# Generated by Django 3.1.8 on 2021-04-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0046_auto_20210408_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='company_address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='invoice',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='invoice',
            name='full_name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='invoice',
            name='iban',
            field=models.CharField(blank=True, max_length=29),
        ),
        migrations.AddField(
            model_name='invoice',
            name='identification_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='mfo',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='invoice',
            name='person_status',
            field=models.CharField(blank=True, max_length=23),
        ),
    ]
