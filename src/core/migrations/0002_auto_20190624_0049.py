# Generated by Django 2.2.2 on 2019-06-23 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'publish')], default='D', max_length=1),
        ),
    ]
