# Generated by Django 4.0.4 on 2022-08-29 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likelionyonsei_app', '0014_alter_member_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='order',
        ),
    ]
