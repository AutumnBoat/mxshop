# Generated by Django 2.1.4 on 2018-12-26 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20181219_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.OrderInfo', verbose_name='order info'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('WAIT_BUYER_PAY', '交易创建'), ('TRADE_SUCCESS', '支付成功'), ('TRADE_FINISHED', '交易完成'), ('TRADE_CLOSED', '交易关闭'), ('paying', '待支付')], default='paying', max_length=20, verbose_name='pay status'),
        ),
    ]