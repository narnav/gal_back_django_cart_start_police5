# Generated by Django 4.0.6 on 2023-06-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('desc', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='quantity',
            new_name='amount',
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
    ]
