# Generated by Django 4.1.4 on 2022-12-26 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_remove_customuser_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bvn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bvn', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=70, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.IntegerField(null=True)),
                ('fpage', models.ImageField(blank=True, null=True, upload_to='')),
                ('bpage', models.ImageField(blank=True, null=True, upload_to='')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business.customerdetails')),
            ],
            options={
                'verbose_name_plural': 'Picture',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_question', models.CharField(max_length=255, null=True)),
                ('security_answer', models.CharField(max_length=255, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business.customerdetails')),
            ],
            options={
                'verbose_name_plural': 'Security Details',
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='bvn',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business.customerdetails'),
        ),
    ]
