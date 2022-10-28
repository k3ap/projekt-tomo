# Generated by Django 4.1.2 on 2022-10-28 12:49

from django.db import migrations, models
import simple_history.models
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField(blank=True)),
                ('valid', models.BooleanField(default=False)),
                ('feedback', models.TextField(default='[]', validators=[utils.is_json_string_list])),
                ('submission_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAttempt',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('solution', models.TextField(blank=True)),
                ('valid', models.BooleanField(default=False)),
                ('feedback', models.TextField(default='[]', validators=[utils.is_json_string_list])),
                ('submission_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical attempt',
                'verbose_name_plural': 'historical attempts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
