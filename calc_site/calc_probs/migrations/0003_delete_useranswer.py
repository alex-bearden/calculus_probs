# Generated by Django 4.0.4 on 2022-05-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc_probs', '0002_integralquestion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]