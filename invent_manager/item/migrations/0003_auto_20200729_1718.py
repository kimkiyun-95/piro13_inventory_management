# Generated by Django 3.0.8 on 2020-07-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20200729_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='item/image', verbose_name='이미지'),
        ),
    ]
