# Generated by Django 3.2.5 on 2021-10-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0023_alter_medals_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_men',
            name='sport',
            field=models.CharField(choices=[('Cricket', 'Cricket'), ('Football', 'Football'), ('Hockey', 'Hockey'), ('Badminton', 'Badminton'), ('Volleyball', 'Volleyball')], default='', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('Japan', 'Japan'), ('China', 'China'), ('Usa', 'Usa'), ('Russia', 'Russia')], max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='sport',
            field=models.CharField(choices=[('Cricket', 'Cricket'), ('Football', 'Football'), ('Hockey', 'Hockey'), ('Badminton', 'Badminton'), ('Volleyball', 'Volleyball')], max_length=32),
        ),
    ]