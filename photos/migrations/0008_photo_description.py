# Generated by Django 2.2 on 2019-05-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20190512_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
