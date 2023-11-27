# Generated by Django 4.2.6 on 2023-11-27 11:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_blog_posted_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 14, 28, 34, 244282), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 14, 28, 34, 245252), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 14, 28, 34, 246282), verbose_name='Дата заказа'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_quantity', models.FloatField(verbose_name='Цена за количество')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order', verbose_name='Заказ')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
                'db_table': 'OrderItems',
                'ordering': ['order_id'],
            },
        ),
    ]
