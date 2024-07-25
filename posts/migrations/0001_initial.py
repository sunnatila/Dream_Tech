# Generated by Django 5.0.6 on 2024-07-24 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/images/', verbose_name='Rasm')),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Tavsifi')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Tavsifi')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Tavsifi')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Tavsifi')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Narxi')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Manzil')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Boshlangan kuni')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Yakunlangan kuni')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
            ],
            options={
                'verbose_name': 'Loyiha ',
                'verbose_name_plural': 'Loyihalar',
                'db_table': 'projects',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Project_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=60, verbose_name='Proektning nomi')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('description_uz', models.TextField(null=True, verbose_name='Tavsifi')),
                ('description_ru', models.TextField(null=True, verbose_name='Tavsifi')),
                ('description_en', models.TextField(null=True, verbose_name='Tavsifi')),
            ],
            options={
                'verbose_name': 'Loyiha Turini ',
                'verbose_name_plural': 'Loyihalar Turlari',
                'db_table': 'project_types',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name="To'liq ism")),
                ('date', models.DateField(verbose_name='Kun')),
                ('comment', models.TextField(verbose_name='Komentariya')),
                ('comment_uz', models.TextField(null=True, verbose_name='Komentariya')),
                ('comment_ru', models.TextField(null=True, verbose_name='Komentariya')),
                ('comment_en', models.TextField(null=True, verbose_name='Komentariya')),
                ('rank', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=3, verbose_name='Baho')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.project', verbose_name='Loyiha')),
            ],
            options={
                'verbose_name': 'Komentariya ',
                'verbose_name_plural': 'Komentariyalar',
                'db_table': 'comments',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/images', verbose_name='Rasm')),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Qoshilgan vaqt')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.project', verbose_name='Loyiha')),
            ],
            options={
                'verbose_name': 'Loyiha Rasimi ',
                'verbose_name_plural': 'Loyihalar Rasimi',
                'db_table': 'project_images',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Sarlavha')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('description_uz', models.TextField(null=True, verbose_name='Tavsifi')),
                ('description_ru', models.TextField(null=True, verbose_name='Tavsifi')),
                ('description_en', models.TextField(null=True, verbose_name='Tavsifi')),
                ('start_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name="Boshlang'ich narx")),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariffs', to='posts.project_type', verbose_name='Proektning tarifi')),
            ],
            options={
                'verbose_name': 'Tarif ',
                'verbose_name_plural': 'Tariflar',
                'db_table': 'tariffs',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, verbose_name="To'liq ism")),
                ('phone', models.CharField(max_length=30, verbose_name='Telefon raqam')),
                ('message', models.TextField(verbose_name='Maqsad')),
                ('status', models.CharField(choices=[('Ariza yuborilgan', 'Ariza yuborilgan'), ('Rad etish', 'Rad etish'), ('Qabul qilingan', 'Qabul qilingan'), ('Kelishilgan', 'Kelishilgan'), ('Kelishilmagan', 'Kelishilmagan'), ('Davom etayotgan proyekt', 'Davom etayotgan proyekt'), ('Tugatilgan proyekt', 'Tugatilgan proyekt')], default='Ariza yuborilgan', max_length=30, verbose_name='Holati')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='Jonatilgan vaqti')),
                ('project_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.project_type', verbose_name='Loyiha turi')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tariff', verbose_name='Tarif')),
            ],
            options={
                'verbose_name': 'Buyurtma ',
                'verbose_name_plural': 'Buyurtmalar',
                'db_table': 'orders',
            },
        ),
    ]