# Generated by Django 5.0.6 on 2024-08-29 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0008_rename_partdoor_addconsignment_partydoor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addconsignment',
            old_name='godown',
            new_name='delivery',
        ),
        migrations.RenameField(
            model_name='addconsignmenttemp',
            old_name='godown',
            new_name='delivery',
        ),
        migrations.RemoveField(
            model_name='addconsignment',
            name='partydoor',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='partydoor',
        ),
    ]