# Generated by Django 2.1.7 on 2019-03-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
