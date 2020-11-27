# Generated by Django 3.1.2 on 2020-10-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201029_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('groceries', 'Groceries'), ('health', 'Health & Beauty'), ('home', 'Home & Office'), ('phones', 'Phones & Tablets'), ('computing', 'Computing'), ('electronics', 'Electronics'), ('fashion', 'Fashion'), ('baby', 'Baby Products'), ('gaming', 'Gaming'), ('sporting', 'Sporting Goods'), ('automobile', 'Automobile'), ('other', 'Other')], max_length=50),
        ),
    ]
