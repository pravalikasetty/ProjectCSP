# Generated by Django 5.0.6 on 2024-06-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_register_id_register_desig_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='desig',
            field=models.CharField(default='admin', max_length=15),
        ),
    ]
