# Generated by Django 2.1.4 on 2019-09-01 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20190901_0933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodsImage',
            new_name='DetailSlide',
        ),
        migrations.RenameModel(
            old_name='Banner',
            new_name='IndexSlide',
        ),
    ]