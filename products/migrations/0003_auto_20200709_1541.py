# Generated by Django 3.0.8 on 2020-07-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200708_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='files',
            field=models.ImageField(upload_to='product_photos'),
        ),
    ]
