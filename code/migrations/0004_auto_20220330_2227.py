# Generated by Django 3.2.5 on 2022-03-30 18:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code', '0003_auto_20220321_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='code_content',
        ),
        migrations.AlterField(
            model_name='code',
            name='code',
            field=ckeditor.fields.RichTextField(),
        ),
    ]