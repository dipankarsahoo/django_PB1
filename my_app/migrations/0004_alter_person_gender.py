# Generated by Django 4.1.7 on 2023-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'others')], default=1),
        ),
    ]
