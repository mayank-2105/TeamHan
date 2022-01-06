# Generated by Django 2.2.26 on 2022-01-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ne110MAdmin0Countries',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('featurecla', models.CharField(blank=True, max_length=15, null=True)),
                ('scalerank', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('labelrank', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('sovereignt', models.CharField(blank=True, max_length=32, null=True)),
                ('sov_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_dif', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('level', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('type', models.CharField(blank=True, max_length=17, null=True)),
                ('admin', models.CharField(blank=True, max_length=35, null=True)),
                ('adm0_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('geou_dif', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('geounit', models.CharField(blank=True, max_length=35, null=True)),
                ('gu_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('su_dif', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('subunit', models.CharField(blank=True, max_length=35, null=True)),
                ('su_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('brk_diff', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('name', models.CharField(blank=True, max_length=24, null=True)),
                ('name_long', models.CharField(blank=True, max_length=35, null=True)),
                ('brk_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('brk_name', models.CharField(blank=True, max_length=32, null=True)),
                ('brk_group', models.CharField(blank=True, max_length=1, null=True)),
                ('abbrev', models.CharField(blank=True, max_length=10, null=True)),
                ('postal', models.CharField(blank=True, max_length=4, null=True)),
                ('formal_en', models.CharField(blank=True, max_length=52, null=True)),
                ('formal_fr', models.CharField(blank=True, max_length=35, null=True)),
                ('name_ciawf', models.CharField(blank=True, max_length=33, null=True)),
                ('note_adm0', models.CharField(blank=True, max_length=22, null=True)),
                ('note_brk', models.CharField(blank=True, max_length=36, null=True)),
                ('name_sort', models.CharField(blank=True, max_length=35, null=True)),
                ('name_alt', models.CharField(blank=True, max_length=14, null=True)),
                ('mapcolor7', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('mapcolor8', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('mapcolor9', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('mapcolor13', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('pop_est', models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True)),
                ('pop_rank', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('pop_year', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('gdp_md', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('gdp_year', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('economy', models.CharField(blank=True, max_length=26, null=True)),
                ('income_grp', models.CharField(blank=True, max_length=23, null=True)),
                ('fips_10', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_a2', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_a2_eh', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_a3_eh', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_n3', models.CharField(blank=True, max_length=3, null=True)),
                ('iso_n3_eh', models.CharField(blank=True, max_length=3, null=True)),
                ('un_a3', models.CharField(blank=True, max_length=4, null=True)),
                ('wb_a2', models.CharField(blank=True, max_length=3, null=True)),
                ('wb_a3', models.CharField(blank=True, max_length=3, null=True)),
                ('woe_id', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('woe_id_eh', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('woe_note', models.CharField(blank=True, max_length=167, null=True)),
                ('adm0_a3_is', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_us', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_fr', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ru', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_es', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_cn', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_tw', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_in', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_np', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_pk', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_de', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_gb', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_br', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_il', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ps', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_sa', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_eg', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ma', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_pt', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ar', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_jp', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ko', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_vn', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_tr', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_id', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_pl', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_gr', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_it', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_nl', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_se', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_bd', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_ua', models.CharField(blank=True, max_length=3, null=True)),
                ('adm0_a3_un', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('adm0_a3_wb', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('continent', models.CharField(blank=True, max_length=23, null=True)),
                ('region_un', models.CharField(blank=True, max_length=10, null=True)),
                ('subregion', models.CharField(blank=True, max_length=25, null=True)),
                ('region_wb', models.CharField(blank=True, max_length=26, null=True)),
                ('name_len', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('long_len', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('abbrev_len', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('tiny', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('homepart', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('min_zoom', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('min_label', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('max_label', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('ne_id', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('wikidataid', models.CharField(blank=True, max_length=7, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=57, null=True)),
                ('name_bn', models.CharField(blank=True, max_length=105, null=True)),
                ('name_de', models.CharField(blank=True, max_length=40, null=True)),
                ('name_en', models.CharField(blank=True, max_length=35, null=True)),
                ('name_es', models.CharField(blank=True, max_length=41, null=True)),
                ('name_fa', models.CharField(blank=True, max_length=62, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=44, null=True)),
                ('name_el', models.CharField(blank=True, max_length=72, null=True)),
                ('name_he', models.CharField(blank=True, max_length=68, null=True)),
                ('name_hi', models.CharField(blank=True, max_length=97, null=True)),
                ('name_hu', models.CharField(blank=True, max_length=40, null=True)),
                ('name_id', models.CharField(blank=True, max_length=39, null=True)),
                ('name_it', models.CharField(blank=True, max_length=36, null=True)),
                ('name_ja', models.CharField(blank=True, max_length=36, null=True)),
                ('name_ko', models.CharField(blank=True, max_length=33, null=True)),
                ('name_nl', models.CharField(blank=True, max_length=29, null=True)),
                ('name_pl', models.CharField(blank=True, max_length=47, null=True)),
                ('name_pt', models.CharField(blank=True, max_length=39, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=86, null=True)),
                ('name_sv', models.CharField(blank=True, max_length=28, null=True)),
                ('name_tr', models.CharField(blank=True, max_length=41, null=True)),
                ('name_uk', models.CharField(blank=True, max_length=82, null=True)),
                ('name_ur', models.CharField(blank=True, max_length=66, null=True)),
                ('name_vi', models.CharField(blank=True, max_length=56, null=True)),
                ('name_zh', models.CharField(blank=True, max_length=33, null=True)),
                ('name_zht', models.CharField(blank=True, max_length=33, null=True)),
                ('fclass_iso', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_us', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_fr', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ru', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_es', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_cn', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_tw', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_in', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_np', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_pk', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_de', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_gb', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_br', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_il', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ps', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_sa', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_eg', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ma', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_pt', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ar', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_jp', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ko', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_vn', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_tr', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_id', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_pl', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_gr', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_it', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_nl', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_se', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_bd', models.CharField(blank=True, max_length=12, null=True)),
                ('fclass_ua', models.CharField(blank=True, max_length=12, null=True)),
                ('wkb_geometry', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ne_110m_admin_0_countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
        ),
    ]