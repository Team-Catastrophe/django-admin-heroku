# Generated by Django 2.2.7 on 2020-02-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200204_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='quiz_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
