# Generated by Django 3.0.5 on 2020-05-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greened_blog', '0007_auto_20200502_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catlog',
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
