# Generated by Django 5.0.2 on 2024-03-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0004_atta_oil_dairy_food_frozen_food_masala_dryfruits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cool_Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discount', models.IntegerField(default=0)),
                ('ImageSrc', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Info', models.CharField(max_length=255)),
                ('Actual_Price', models.IntegerField(default=0)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
