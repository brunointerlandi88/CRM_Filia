# Generated by Django 3.2.1 on 2021-05-11 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_alter_cliente_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_ins',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
