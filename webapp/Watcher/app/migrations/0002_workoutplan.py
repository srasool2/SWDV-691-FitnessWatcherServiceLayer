# Generated by Django 2.1.7 on 2019-03-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('workout_id', models.AutoField(primary_key=True, serialize=False)),
                ('workout_name', models.CharField(max_length=20)),
                ('workout_duration', models.IntegerField(default=45)),
            ],
            options={
                'db_table': 'workout_plan',
                'managed': True,
            },
        ),
    ]
