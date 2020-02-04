# Generated by Django 2.2.7 on 2020-02-03 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0005_auto_20200203_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Fill in the blank Question',
                'verbose_name_plural': 'Fill in the blank Question',
            },
            bases=('quiz.question',),
        ),
        migrations.CreateModel(
            name='FillAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(help_text='Fill in the blanks answer', max_length=1000, verbose_name='Content')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fillintheblanks.FillQuestion', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]