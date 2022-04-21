# Generated by Django 2.2.5 on 2022-04-21 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_auto_20220421_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='calcium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='carbohydrate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='cholesterol',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='energy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='iron',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='magnesium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='phosphorus',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='potassium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sodium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sugars',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='transfat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='zinc',
            field=models.FloatField(null=True),
        ),
    ]
