# Generated by Django 2.2.7 on 2020-02-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillintheblanks', '0003_auto_20200203_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillquestion',
            name='fill',
            field=models.BooleanField(default=True),
        ),
    ]