# Generated by Django 4.0.3 on 2022-04-06 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupen_name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('percent', models.IntegerField()),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('used', models.BooleanField(default=False)),
                ('live', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start', models.BooleanField(default=False)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Admin.categories')),
            ],
        ),
    ]