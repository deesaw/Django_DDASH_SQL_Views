# Generated by Django 3.0.5 on 2020-05-17 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DetailsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='CategoryID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Categories', to='DetailsApp.Category'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='DomainID',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Masters', to='DetailsApp.Master'),
        ),
    ]
