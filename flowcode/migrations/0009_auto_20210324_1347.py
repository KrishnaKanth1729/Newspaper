# Generated by Django 3.1.6 on 2021-03-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowcode', '0008_auto_20210324_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyfile',
            name='color',
            field=models.CharField(default='#fff000', max_length=255),
        ),
    ]