# Generated by Django 3.2.1 on 2021-05-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_myanothermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusermodel',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]