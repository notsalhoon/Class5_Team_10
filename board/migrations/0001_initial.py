# Generated by Django 2.2.5 on 2022-04-22 16:24

import board.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ctg', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField()),
                ('moddate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to=board.models.board_directory_path)),
                ('regdate', models.DateTimeField()),
                ('moddate', models.DateTimeField(blank=True, null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
        ),
    ]
