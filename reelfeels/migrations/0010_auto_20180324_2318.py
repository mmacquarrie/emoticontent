# Generated by Django 2.0.2 on 2018-03-25 03:18

from django.db import migrations, models
import django.db.models.deletion
import reelfeels.models


class Migration(migrations.Migration):

    dependencies = [
        ('reelfeels', '0009_auto_20180227_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.CharField(default='129d2174', editable=False, max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ViewInstance',
            fields=[
                ('id', models.CharField(default='22d747de', editable=False, max_length=8, primary_key=True, serialize=False)),
                ('last_watched', models.DateField(verbose_name='Date updated')),
                ('happiness', models.IntegerField(default=0, verbose_name='Happiness')),
                ('sadness', models.IntegerField(default=0, verbose_name='Sadness')),
                ('disgust', models.IntegerField(default=0, verbose_name='Disgust')),
                ('anger', models.IntegerField(default=0, verbose_name='Anger')),
                ('surprise', models.IntegerField(default=0, verbose_name='Surprise')),
            ],
        ),
        migrations.RemoveField(
            model_name='videotouser',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='videotouser',
            name='video_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='commenter_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='date_updated_emotions',
            new_name='last_updated_emotions',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='last_updated',
            new_name='last_updated_emotions',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='user_id',
            new_name='uploader_id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='total_views',
        ),
        migrations.AddField(
            model_name='video',
            name='todays_views',
            field=models.IntegerField(default=0, verbose_name='Todays views'),
        ),
        migrations.AddField(
            model_name='video',
            name='yesterdays_views',
            field=models.IntegerField(default=0, verbose_name='Yesterdays views'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='51bfc0e8', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='294e3578', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=reelfeels.models.profile_filename),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.CharField(default='10b5509d', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='VideoToUser',
        ),
        migrations.AddField(
            model_name='viewinstance',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reelfeels.Video'),
        ),
        migrations.AddField(
            model_name='viewinstance',
            name='viewer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reelfeels.User'),
        ),
        migrations.AddField(
            model_name='upload',
            name='uploader_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reelfeels.User'),
        ),
        migrations.AddField(
            model_name='upload',
            name='video_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reelfeels.Video'),
        ),
    ]
