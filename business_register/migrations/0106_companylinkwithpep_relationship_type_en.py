# Generated by Django 3.1.8 on 2021-06-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0105_auto_20210520_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='companylinkwithpep',
            name='relationship_type_en',
            field=models.CharField(help_text='Type of connection between the person and this company in English', max_length=550, null=True, verbose_name='connection`s type in English'),
        ),
    ]
