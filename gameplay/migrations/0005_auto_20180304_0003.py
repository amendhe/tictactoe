# Generated by Django 2.0.2 on 2018-03-03 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0004_auto_20180303_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
        ),
    ]
