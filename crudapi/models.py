# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ne110MAdmin0Countries(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    featurecla = models.CharField(max_length=15, blank=True, null=True)
    scalerank = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    labelrank = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sovereignt = models.CharField(max_length=32, blank=True, null=True)
    sov_a3 = models.CharField(max_length=3, blank=True, null=True)
    adm0_dif = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    level = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    type = models.CharField(max_length=17, blank=True, null=True)
    admin = models.CharField(max_length=35, blank=True, null=True)
    adm0_a3 = models.CharField(max_length=3, blank=True, null=True)
    geou_dif = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    geounit = models.CharField(max_length=35, blank=True, null=True)
    gu_a3 = models.CharField(max_length=3, blank=True, null=True)
    su_dif = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    subunit = models.CharField(max_length=35, blank=True, null=True)
    su_a3 = models.CharField(max_length=3, blank=True, null=True)
    brk_diff = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=24, blank=True, null=True)
    name_long = models.CharField(max_length=35, blank=True, null=True)
    brk_a3 = models.CharField(max_length=3, blank=True, null=True)
    brk_name = models.CharField(max_length=32, blank=True, null=True)
    brk_group = models.CharField(max_length=1, blank=True, null=True)
    abbrev = models.CharField(max_length=10, blank=True, null=True)
    postal = models.CharField(max_length=4, blank=True, null=True)
    formal_en = models.CharField(max_length=52, blank=True, null=True)
    formal_fr = models.CharField(max_length=35, blank=True, null=True)
    name_ciawf = models.CharField(max_length=33, blank=True, null=True)
    note_adm0 = models.CharField(max_length=22, blank=True, null=True)
    note_brk = models.CharField(max_length=36, blank=True, null=True)
    name_sort = models.CharField(max_length=35, blank=True, null=True)
    name_alt = models.CharField(max_length=14, blank=True, null=True)
    mapcolor7 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    mapcolor8 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    mapcolor9 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    mapcolor13 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    pop_est = models.DecimalField(max_digits=12, decimal_places=1, blank=True, null=True)
    pop_rank = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    pop_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    gdp_md = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    gdp_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    economy = models.CharField(max_length=26, blank=True, null=True)
    income_grp = models.CharField(max_length=23, blank=True, null=True)
    fips_10 = models.CharField(max_length=3, blank=True, null=True)
    iso_a2 = models.CharField(max_length=3, blank=True, null=True)
    iso_a2_eh = models.CharField(max_length=3, blank=True, null=True)
    iso_a3 = models.CharField(max_length=3, blank=True, null=True)
    iso_a3_eh = models.CharField(max_length=3, blank=True, null=True)
    iso_n3 = models.CharField(max_length=3, blank=True, null=True)
    iso_n3_eh = models.CharField(max_length=3, blank=True, null=True)
    un_a3 = models.CharField(max_length=4, blank=True, null=True)
    wb_a2 = models.CharField(max_length=3, blank=True, null=True)
    wb_a3 = models.CharField(max_length=3, blank=True, null=True)
    woe_id = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    woe_id_eh = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    woe_note = models.CharField(max_length=167, blank=True, null=True)
    adm0_a3_is = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_us = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_fr = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ru = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_es = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_cn = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_tw = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_in = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_np = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_pk = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_de = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_gb = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_br = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_il = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ps = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_sa = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_eg = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ma = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_pt = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ar = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_jp = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ko = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_vn = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_tr = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_id = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_pl = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_gr = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_it = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_nl = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_se = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_bd = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_ua = models.CharField(max_length=3, blank=True, null=True)
    adm0_a3_un = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    adm0_a3_wb = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    continent = models.CharField(max_length=23, blank=True, null=True)
    region_un = models.CharField(max_length=10, blank=True, null=True)
    subregion = models.CharField(max_length=25, blank=True, null=True)
    region_wb = models.CharField(max_length=26, blank=True, null=True)
    name_len = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    long_len = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    abbrev_len = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    tiny = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    homepart = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    min_zoom = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    min_label = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    max_label = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ne_id = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wikidataid = models.CharField(max_length=7, blank=True, null=True)
    name_ar = models.CharField(max_length=57, blank=True, null=True)
    name_bn = models.CharField(max_length=105, blank=True, null=True)
    name_de = models.CharField(max_length=40, blank=True, null=True)
    name_en = models.CharField(max_length=35, blank=True, null=True)
    name_es = models.CharField(max_length=41, blank=True, null=True)
    name_fa = models.CharField(max_length=62, blank=True, null=True)
    name_fr = models.CharField(max_length=44, blank=True, null=True)
    name_el = models.CharField(max_length=72, blank=True, null=True)
    name_he = models.CharField(max_length=68, blank=True, null=True)
    name_hi = models.CharField(max_length=97, blank=True, null=True)
    name_hu = models.CharField(max_length=40, blank=True, null=True)
    name_id = models.CharField(max_length=39, blank=True, null=True)
    name_it = models.CharField(max_length=36, blank=True, null=True)
    name_ja = models.CharField(max_length=36, blank=True, null=True)
    name_ko = models.CharField(max_length=33, blank=True, null=True)
    name_nl = models.CharField(max_length=29, blank=True, null=True)
    name_pl = models.CharField(max_length=47, blank=True, null=True)
    name_pt = models.CharField(max_length=39, blank=True, null=True)
    name_ru = models.CharField(max_length=86, blank=True, null=True)
    name_sv = models.CharField(max_length=28, blank=True, null=True)
    name_tr = models.CharField(max_length=41, blank=True, null=True)
    name_uk = models.CharField(max_length=82, blank=True, null=True)
    name_ur = models.CharField(max_length=66, blank=True, null=True)
    name_vi = models.CharField(max_length=56, blank=True, null=True)
    name_zh = models.CharField(max_length=33, blank=True, null=True)
    name_zht = models.CharField(max_length=33, blank=True, null=True)
    fclass_iso = models.CharField(max_length=12, blank=True, null=True)
    fclass_us = models.CharField(max_length=12, blank=True, null=True)
    fclass_fr = models.CharField(max_length=12, blank=True, null=True)
    fclass_ru = models.CharField(max_length=12, blank=True, null=True)
    fclass_es = models.CharField(max_length=12, blank=True, null=True)
    fclass_cn = models.CharField(max_length=12, blank=True, null=True)
    fclass_tw = models.CharField(max_length=12, blank=True, null=True)
    fclass_in = models.CharField(max_length=12, blank=True, null=True)
    fclass_np = models.CharField(max_length=12, blank=True, null=True)
    fclass_pk = models.CharField(max_length=12, blank=True, null=True)
    fclass_de = models.CharField(max_length=12, blank=True, null=True)
    fclass_gb = models.CharField(max_length=12, blank=True, null=True)
    fclass_br = models.CharField(max_length=12, blank=True, null=True)
    fclass_il = models.CharField(max_length=12, blank=True, null=True)
    fclass_ps = models.CharField(max_length=12, blank=True, null=True)
    fclass_sa = models.CharField(max_length=12, blank=True, null=True)
    fclass_eg = models.CharField(max_length=12, blank=True, null=True)
    fclass_ma = models.CharField(max_length=12, blank=True, null=True)
    fclass_pt = models.CharField(max_length=12, blank=True, null=True)
    fclass_ar = models.CharField(max_length=12, blank=True, null=True)
    fclass_jp = models.CharField(max_length=12, blank=True, null=True)
    fclass_ko = models.CharField(max_length=12, blank=True, null=True)
    fclass_vn = models.CharField(max_length=12, blank=True, null=True)
    fclass_tr = models.CharField(max_length=12, blank=True, null=True)
    fclass_id = models.CharField(max_length=12, blank=True, null=True)
    fclass_pl = models.CharField(max_length=12, blank=True, null=True)
    fclass_gr = models.CharField(max_length=12, blank=True, null=True)
    fclass_it = models.CharField(max_length=12, blank=True, null=True)
    fclass_nl = models.CharField(max_length=12, blank=True, null=True)
    fclass_se = models.CharField(max_length=12, blank=True, null=True)
    fclass_bd = models.CharField(max_length=12, blank=True, null=True)
    fclass_ua = models.CharField(max_length=12, blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ne_110m_admin_0_countries'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'