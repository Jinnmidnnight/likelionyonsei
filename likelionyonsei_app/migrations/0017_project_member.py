# Generated by Django 4.1 on 2022-08-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelionyonsei_app', '0016_alter_member_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
