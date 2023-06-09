# Generated by Django 4.1.5 on 2023-04-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recently',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_product', models.ImageField(upload_to='static/single_product')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('mrp', models.CharField(max_length=10)),
                ('category_one', models.CharField(max_length=100)),
                ('category_two', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='similar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_product', models.ImageField(upload_to='static/single_product')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('mrp', models.CharField(max_length=10)),
                ('category_one', models.CharField(max_length=100)),
                ('category_two', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_product', models.ImageField(upload_to='static/single_product')),
                ('title', models.CharField(max_length=500)),
                ('category_one', models.CharField(max_length=100)),
                ('category_two', models.CharField(max_length=100)),
                ('category_three', models.CharField(max_length=100)),
                ('category_four', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=900)),
                ('price', models.CharField(max_length=100)),
                ('mrp', models.CharField(max_length=100)),
                ('Discount', models.CharField(max_length=100)),
                ('Save', models.CharField(max_length=100)),
                ('Only', models.CharField(max_length=100)),
                ('Available_Color', models.CharField(max_length=100)),
                ('Available_Size', models.CharField(max_length=100)),
                ('Key_Features', models.CharField(max_length=100)),
                ('Sku', models.CharField(max_length=100)),
                ('Main_Material', models.CharField(max_length=100)),
                ('Color', models.CharField(max_length=100)),
                ('Sleeves', models.CharField(max_length=100)),
                ('Top_Fit', models.CharField(max_length=100)),
                ('Print', models.CharField(max_length=100)),
                ('Neck', models.CharField(max_length=100)),
                ('Pieces_Count', models.CharField(max_length=100)),
                ('Occasion', models.CharField(max_length=100)),
                ('Shipping_Weight_kg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='single_product_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_product_image', models.ImageField(upload_to='static/single_product')),
            ],
        ),
    ]
