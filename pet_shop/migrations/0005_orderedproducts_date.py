# Generated by Django 4.2.1 on 2023-06-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop', '0004_orderedproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproducts',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
