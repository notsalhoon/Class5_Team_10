# Generated by Django 2.2.5 on 2022-04-15 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('nutrition_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=30)),
                ('quantity', models.FloatField()),
                ('energy', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('sugars', models.FloatField()),
                ('fat', models.FloatField()),
                ('protein', models.FloatField()),
                ('calcium', models.FloatField()),
                ('phosphorus', models.FloatField()),
                ('sodium', models.FloatField()),
                ('iron', models.FloatField()),
                ('zinc', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('transfat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.AutoField(primary_key=True, serialize=False)),
                ('meal_img', models.CharField(max_length=20)),
                ('meal_regdate', models.DateField()),
                ('meal_time', models.CharField(max_length=20)),
                ('kid_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Kid')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('diet_id', models.AutoField(primary_key=True, serialize=False)),
                ('meal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.Meal')),
                ('nutrition_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meal.Nutrition')),
            ],
        ),
    ]
