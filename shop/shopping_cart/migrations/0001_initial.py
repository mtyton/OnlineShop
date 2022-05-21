# Generated by Django 4.0 on 2021-12-19 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ordered", models.BooleanField(default=False)),
                ("ordered_at", models.DateTimeField(default=None, null=True)),
                ("payed", models.BooleanField(default=False)),
                ("user_notified", models.BooleanField(default=False)),
                (
                    "anonymous_customer",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="users.anonymouscustomer"
                    ),
                ),
                (
                    "registered_customer",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="users.personcustomer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.IntegerField(default=1)),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="shopping_cart.order")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.product")),
            ],
        ),
    ]
