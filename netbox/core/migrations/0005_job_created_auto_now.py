# Generated by Django 4.1.7 on 2023-03-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_replicate_jobresults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]