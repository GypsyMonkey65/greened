# Generated by Django 3.0.5 on 2020-05-02 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greened_blog', '0005_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'articles'},
        ),
    ]
