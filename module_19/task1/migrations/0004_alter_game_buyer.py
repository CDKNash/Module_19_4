# Generated by Django 4.2.17 on 2024-12-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_alter_buyer_balance_alter_game_cost_alter_game_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(to='task1.buyer'),
        ),
    ]