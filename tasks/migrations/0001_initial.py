# Generated by Django 3.0.4 on 2020-03-19 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('last_start', models.DateTimeField(default=None, null=True)),
                ('last_finish', models.DateTimeField(default=None, null=True)),
                ('avg_duration', models.DurationField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='tasks.Task')),
            ],
        ),
    ]
