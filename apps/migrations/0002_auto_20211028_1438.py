# Generated by Django 3.2.8 on 2021-10-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageSS1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageSS2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageSS3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageSS4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
    ]
