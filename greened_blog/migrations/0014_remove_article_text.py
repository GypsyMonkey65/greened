# Generated by Django 3.0.5 on 2020-05-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greened_blog', '0013_article_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='text',
        ),
    ]
