# Generated by Django 4.1 on 2022-08-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("likelionyonsei_app", "0003_recruit_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recruit",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
