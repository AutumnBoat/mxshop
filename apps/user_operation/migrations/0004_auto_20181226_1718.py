# Generated by Django 2.1.4 on 2018-12-26 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20181225_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='商品 id', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='goods'),
        ),
    ]
