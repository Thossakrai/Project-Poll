# Generated by Django 2.0.2 on 2018-03-09 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=300)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=5)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('age_range', models.IntegerField()),
                ('marriage', models.IntegerField()),
                ('education', models.IntegerField()),
                ('live_with', models.IntegerField()),
                ('guardian', models.IntegerField()),
                ('occupation', models.IntegerField()),
                ('income_avg', models.IntegerField()),
                ('chronic_dis', models.IntegerField()),
                ('chronic_dis_detail', models.CharField(default='', max_length=100)),
                ('chronic_dis_time', models.IntegerField()),
                ('medi_number', models.IntegerField()),
                ('hyperventi_medi', models.IntegerField()),
                ('fall_hist', models.IntegerField()),
                ('score_profile', models.IntegerField()),
                ('finished', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_set_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.QuestionSet'),
        ),
        migrations.AddField(
            model_name='answerset',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_set_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.AnswerSet'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
