# Generated by Django 3.2.5 on 2022-04-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20220404_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='language_fields',
        ),
        migrations.AddField(
            model_name='language',
            name='language_fields',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]