# Generated by Django 2.2.2 on 2019-07-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]
