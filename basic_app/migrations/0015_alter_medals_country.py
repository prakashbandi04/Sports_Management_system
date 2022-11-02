# Generated by Django 3.2.5 on 2021-09-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0014_auto_20210902_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medals',
            name='country',
            field=models.CharField(choices=[('Ind', 'India'), ('Jpn', 'Japan'), ('Chn', 'China'), ('Usa', 'Usa'), ('Rs', 'Russia')], default='', max_length=32),
        ),
    ]