# Generated by Django 4.2.6 on 2023-11-26 21:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_blog_posted_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 0, 18, 36, 863039), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 0, 18, 36, 864037), verbose_name='Дата комментария'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Comments',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 27, 0, 18, 36, 864037), verbose_name='Дата заказа')),
                ('total_price', models.FloatField(verbose_name='Итоговая сумма заказа')),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Статус заказа')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'Order',
                'ordering': ['date'],
            },
        ),
    ]