# Generated by Django 3.2.6 on 2021-09-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to='static/uplods'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=200),
        ),
    ]
