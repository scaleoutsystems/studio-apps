# Generated by Django 3.1.7 on 2021-05-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0052_remove_appinstance_release_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='chart_archive',
            field=models.FileField(blank=True, null=True, upload_to='apps/'),
        ),
        migrations.AddField(
            model_name='apps',
            name='revision',
            field=models.IntegerField(default=1),
        ),
    ]
