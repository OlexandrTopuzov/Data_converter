# Generated by Django 3.1.8 on 2021-04-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0091_auto_20210426_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personsanction',
            name='id_card',
            field=models.TextField(blank=True, default='', help_text='id cards info of the person under sanctions', verbose_name='id cards info'),
        ),
    ]
