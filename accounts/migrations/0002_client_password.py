# Generated by Django 3.1.4 on 2021-06-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Password',
            field=models.CharField(default='ohhfaf', max_length=20),
            preserve_default=False,
        ),
    ]
