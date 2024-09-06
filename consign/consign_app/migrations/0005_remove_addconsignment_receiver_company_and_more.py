# Generated by Django 5.0.6 on 2024-08-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0004_consignee_branch_consignor_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addconsignment',
            name='receiver_company',
        ),
        migrations.RemoveField(
            model_name='addconsignment',
            name='receiver_email',
        ),
        migrations.RemoveField(
            model_name='addconsignment',
            name='sender_company',
        ),
        migrations.RemoveField(
            model_name='addconsignment',
            name='sender_email',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='receiver_company',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='receiver_email',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='sender_company',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='sender_email',
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='weightAmt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='weightAmt',
            field=models.IntegerField(null=True),
        ),
    ]