# Generated by Django 3.0.5 on 2020-04-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greened_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catlog_1st_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greened_blog.Topic')),
            ],
            options={
                'verbose_name_plural': 'catlog_1st_level',
            },
        ),
        migrations.CreateModel(
            name='Catlog_2nd_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greened_blog.Catlog_1st_Level')),
            ],
            options={
                'verbose_name_plural': 'catlog_2nd_level',
            },
        ),
    ]
