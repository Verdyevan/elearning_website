# Generated by Django 2.2.10 on 2020-05-31 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200601_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comment_count',
            field=models.IntegerField(),
        ),
    ]
