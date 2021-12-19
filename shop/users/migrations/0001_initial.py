# Generated by Django 4.0 on 2021-12-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=12)),
                ('building_number', models.CharField(max_length=10)),
                ('flat_number', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=12)),
                ('building_number', models.CharField(max_length=10)),
                ('flat_number', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]