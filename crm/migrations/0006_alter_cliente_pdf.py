# Generated by Django 3.2.1 on 2021-05-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20210507_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]