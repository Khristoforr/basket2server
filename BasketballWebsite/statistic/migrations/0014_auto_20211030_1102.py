# Generated by Django 3.2.7 on 2021-10-30 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0013_auto_20211024_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagestat',
            name='ast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='blk',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='dreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='eff',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fg3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fga3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fgm3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='ft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='fta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='ftm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='oreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='plus_minus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='pts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='reb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='stl',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='averagestat',
            name='tov',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='ast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='blk',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='dreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='eff',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fg2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fg3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fga2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fga3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fgm2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fgm3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='ft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='fta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='ftm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='oreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='plus_minus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='pts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='reb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='stl',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game1',
            name='tov',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='ast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='blk',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='dreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='eff',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fg2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fg3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fga2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fga3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fgm2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fgm3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='ft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='fta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='ftm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='oreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='plus_minus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='pts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='reb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='stl',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game2',
            name='tov',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='ast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='blk',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='dreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='eff',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fg2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fg3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fga2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fga3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fgm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fgm2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fgm3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='ft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='fta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='ftm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='oreb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='plus_minus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='pts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='reb',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='stl',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='game3',
            name='tov',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_players', to='statistic.team'),
        ),
    ]
