# Generated by Django 2.2.1 on 2019-05-28 08:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')]),
        ),
    ]
