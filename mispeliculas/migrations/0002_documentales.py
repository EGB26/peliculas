# Generated by Django 4.1.5 on 2023-02-14 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mispeliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0)),
                ('temporada', models.IntegerField(default=0)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mispeliculas.serie')),
            ],
        ),
    ]