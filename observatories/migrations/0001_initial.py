# Generated by Django 3.1.2 on 2021-01-23 22:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observatory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('name_kana', models.CharField(max_length=200)),
                ('code', models.IntegerField()),
                ('observation_type', models.CharField(max_length=4)),
                ('prefecture', models.IntegerField(choices=[(1, '北海道'), (2, '青森県'), (3, '岩手県'), (4, '宮城県'), (5, '秋田県'), (6, '山形県'), (7, '福島県'), (8, '茨城県'), (9, '栃木県'), (10, '群馬県'), (11, '埼玉県'), (12, '千葉県'), (13, '東京都'), (14, '神奈川県'), (15, '新潟県'), (16, '富山県'), (17, '石川県'), (18, '福井県'), (19, '山梨県'), (20, '長野県'), (21, '岐阜県'), (22, '静岡県'), (23, '愛知県'), (24, '三重県'), (25, '滋賀県'), (26, '京都府'), (27, '大阪府'), (28, '兵庫県'), (29, '奈良県'), (30, '和歌山県'), (31, '鳥取県'), (32, '島根県'), (33, '岡山県'), (34, '広島県'), (35, '山口県'), (36, '徳島県'), (37, '香川県'), (38, '愛媛県'), (39, '高知県'), (40, '福岡県'), (41, '佐賀県'), (42, '長崎県'), (43, '熊本県'), (44, '大分県'), (45, '宮崎県'), (46, '鹿児島県'), (47, '沖縄県')])),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'verbose_name_plural': 'Observatories',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observed_at', models.DateTimeField()),
                ('highest', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('highest_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('highest_observed_at', models.DateTimeField()),
                ('lowest', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('lowest_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('lowest_observed_at', models.DateTimeField()),
                ('observatory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='observatory_temperature', to='observatories.observatory')),
            ],
        ),
        migrations.CreateModel(
            name='Snowfall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observed_at', models.DateTimeField()),
                ('snowfall_3h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_3h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('snowfall_6h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_6h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('snowfall_12h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_12h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('snowfall_24h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_24h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('snowfall_48h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_48h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('snowfall_72h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('snowfall_72h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('observatory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='observatory_snowfall', to='observatories.observatory')),
            ],
        ),
        migrations.CreateModel(
            name='SnowDepth',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observed_at', models.DateTimeField()),
                ('snow_depth', models.IntegerField(blank=True, null=True)),
                ('snow_depth_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('ratio_compared_to_normal', models.IntegerField(blank=True, null=True)),
                ('observatory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='observatory_snow_depth', to='observatories.observatory')),
            ],
        ),
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observed_at', models.DateTimeField()),
                ('rainfall_3h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_3h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('rainfall_6h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_6h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('rainfall_12h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_12h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('rainfall_24h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_24h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('rainfall_48h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_48h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('rainfall_72h', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('rainfall_72h_quality_level', models.IntegerField(blank=True, choices=[(0, '統計しない'), (1, '資料なし、未報告'), (2, '利用不適値'), (3, '疑問値'), (4, '資料不足値'), (5, '準正常値'), (8, '正常値')], null=True)),
                ('observatory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='observatory_rainfall', to='observatories.observatory')),
            ],
        ),
    ]