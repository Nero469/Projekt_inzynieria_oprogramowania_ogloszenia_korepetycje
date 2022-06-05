# Generated by Django 4.0.5 on 2022-06-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
