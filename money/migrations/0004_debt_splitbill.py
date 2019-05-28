# Generated by Django 2.1.3 on 2019-05-28 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money', '0003_auto_20190528_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('type_of_debt', models.CharField(choices=[('given', 'Given'), ('take', 'Take')], max_length=50)),
                ('debt_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debt_to_user', to=settings.AUTH_USER_MODEL)),
                ('debt_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debt_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SplitBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('no_0f_people', models.PositiveIntegerField()),
                ('split_amount', models.PositiveIntegerField()),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
