# Generated by Django 5.0.6 on 2024-08-31 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0013_addconsignment_eway_bill_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Driver',
        ),
    ]