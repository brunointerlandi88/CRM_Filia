# Generated by Django 3.2 on 2021-05-04 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clienti'},
        ),
    ]
