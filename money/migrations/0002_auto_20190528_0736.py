# Generated by Django 2.1.3 on 2019-05-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackexpenses',
            name='user',
            field=models.CharField(blank=True, max_length=253),
        ),
    ]
