# Generated by Django 3.2.5 on 2021-09-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0016_auto_20210902_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='medals',
            name='total_meadals',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
