# Generated by Django 2.0 on 2018-12-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='video_link',
            field=models.CharField(max_length=200, null=True, verbose_name='Video Link'),
        ),
    ]
