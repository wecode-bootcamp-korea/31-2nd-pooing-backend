# Generated by Django 4.0.3 on 2022-04-12 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('thumbnail_image_url', models.URLField(max_length=2000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.category')),
            ],
            options={
                'db_table': 'lectures',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'schedules',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='TypeLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.type')),
            ],
            options={
                'db_table': 'types_lectures',
            },
        ),
        migrations.CreateModel(
            name='ScheduleLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.schedule')),
            ],
            options={
                'db_table': 'schedules_lectures',
            },
        ),
        migrations.CreateModel(
            name='RegionLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.region')),
            ],
            options={
                'db_table': 'regions_lectures',
            },
        ),
        migrations.CreateModel(
            name='LectureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(max_length=2000)),
                ('sequence', models.PositiveIntegerField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
            ],
            options={
                'db_table': 'lecture_images',
            },
        ),
        migrations.AddField(
            model_name='lecture',
            name='regions',
            field=models.ManyToManyField(through='lectures.RegionLecture', to='lectures.region'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='schedules',
            field=models.ManyToManyField(through='lectures.ScheduleLecture', to='lectures.schedule'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='types',
            field=models.ManyToManyField(through='lectures.TypeLecture', to='lectures.type'),
        ),
    ]