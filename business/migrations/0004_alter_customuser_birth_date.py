# Generated by Django 4.1.4 on 2022-12-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_customuser_bpage_customuser_fpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
