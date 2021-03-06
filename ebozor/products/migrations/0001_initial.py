# Generated by Django 3.2.8 on 2021-10-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Name')),
                ('photo', models.CharField(max_length=255, null=True, verbose_name='Photo ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(null=True)),
                ('category_code', models.CharField(max_length=50)),
                ('category_name', models.CharField(max_length=50)),
                ('subcategory_code', models.CharField(max_length=50)),
                ('subcategory_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Telegram Username')),
                ('telegram_id', models.BigIntegerField(unique=True, verbose_name='Telegram ID')),
            ],
        ),
    ]
