# Generated by Django 4.1 on 2022-08-18 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='work',
        ),
        migrations.AddField(
            model_name='employer',
            name='person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.person'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(to='main.employer'),
        ),
    ]
