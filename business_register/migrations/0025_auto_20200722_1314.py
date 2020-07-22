# Generated by Django 3.0.7 on 2020-07-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0024_auto_20200720_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignee',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='bancruptcyreadjustment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='bylaw',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='companydetail',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='companytokved',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='companytopredecessor',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='companytype',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='exchangedatacompany',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='exchangedatafop',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='fop',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='foptokved',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='founder',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='founders',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='historicalfounder',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical founder'},
        ),
        migrations.AlterModelOptions(
            name='kved',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='kveddivision',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='kvedgroup',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='kvedsection',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='predecessor',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='rfop',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='ruo',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='signer',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='terminationstarted',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='founder',
            name='info',
            field=models.CharField(max_length=2015),
        ),
        migrations.AlterField(
            model_name='historicalfounder',
            name='info',
            field=models.CharField(max_length=2015),
        ),
    ]
