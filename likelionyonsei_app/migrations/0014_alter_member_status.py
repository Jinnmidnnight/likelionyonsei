# Generated by Django 4.0.4 on 2022-08-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelionyonsei_app', '0013_member_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '일반 구성원'), (1, '운영진'), (2, '부대포'), (3, '대표')], default=0),
        ),
    ]
