# Generated by Django 4.0.4 on 2022-05-26 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc_probs', '0005_rename_user_answer_useranswer_user_answer_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
