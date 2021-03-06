# Generated by Django 2.1 on 2018-09-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedstoneArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='ArticleTitle', max_length=128)),
                ('url', models.CharField(default='ArticleURL', max_length=1024)),
                ('content', models.TextField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('up_vote', models.PositiveIntegerField(default=0)),
                ('down_vote', models.PositiveIntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'rs_article',
            },
        ),
        migrations.CreateModel(
            name='RedstoneFeedsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default RSS Name', max_length=64)),
                ('url', models.CharField(default='', max_length=1024)),
                ('fetch_time', models.DateTimeField(default='')),
                ('interval', models.IntegerField(default=30)),
                ('alive_status', models.IntegerField(default=0)),
                ('spider_type', models.IntegerField(default=0)),
                ('fail_reason', models.CharField(max_length=512)),
                ('use_proxy', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'rs_feeds',
            },
        ),
        migrations.CreateModel(
            name='RedstoneSpiderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default Spider', max_length=128)),
                ('spider_name', models.CharField(db_index=True, default='SpiderName', max_length=128)),
                ('filename', models.CharField(default='default_rss.py', max_length=256)),
                ('class_name', models.CharField(default='DefaultRSSClassName', max_length=256)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'rs_spider',
            },
        ),
    ]
