# Generated by Django 3.0.7 on 2020-07-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0006_auto_20200724_1128'),
        ('business_register', '0026_auto_20200727_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangedatafop',
            name='authority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_ocean.Authority', verbose_name='орган реєстрації'),
        ),
    ]
