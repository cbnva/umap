# Written by Jeremy Lee, 2020-10-30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umap', '0007_auto_20190416_1757'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='share_status',
            field=models.SmallIntegerField(choices=[(1, 'everyone (public)'), (2, 'anyone with link'), (3, 'editors only'), (4, 'viewers and editors'), (5, 'authenticated'), (9, 'blocked')], default=1, verbose_name='share status'),
        ),
        migrations.AddField(
            model_name='map',
            name='viewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='viewers', related_name='map_viewers'),
        ),
        migrations.AlterField(
            model_name='map',
            name='editors',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='editors', related_name='map_editors'),
        ),
    ]
