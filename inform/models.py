# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


# Create your models here.
class SoatoData(models.Model):
    id_soato = models.AutoField(primary_key=True)
    soato_kode = models.CharField('Код СОATO',max_length=10)
    soato_name = models.CharField('Название',max_length=200)
    soato_nameadd = models.CharField('Название дополнительное', max_length=200)

    class Meta:
        db_table = u'SoatoData'
        verbose_name = 'Данные по коду СОAТО'
        verbose_name_plural = 'Данные по кодам СОАТО'

    def __unicode__(self):
        return u" %s  %s  %s " % (self.soato_nameadd,self.soato_name,self.soato_kode)


class EntDbSpr(models.Model):
    id_entdbspr = models.AutoField(primary_key=True)
    npr = models.CharField('Полное наименование юридического лица', max_length=400)
    adr = models.CharField('Почтовый адрес (фактический)', max_length=400)
    okp = models.CharField('Регистрационный номер респондента (ОКПО)',max_length=400)
    oku = models.CharField('Учетный номер плательщика (УНП)',max_length=400)
    gup = models.CharField(' Код респондента по государственного водному кадастру (ГВК)',max_length=400)
    tel = models.CharField(' Телефон ',max_length=400)
    vxu = models.CharField('Водохозяйственынй участок',max_length=400)



class Page1(models.Model):
    id_page1 = models.AutoField(primary_key=True)
    wateruser_name = models.CharField('Полное наименование юридического лица', max_length=400)
    wateruser_level_name = models.CharField('Полное наименование обособленного подразделения юридического лица', max_length=400)
    postal_address = models.CharField('Почтовый адрес (фактический)', max_length=400)
    email_address = models.CharField('Электронный адрес (e-mail)', max_length=400)
    territory_level = models.CharField('Территория нахождения структурного подразделения', max_length=400)
    kod_soato = models.ForeignKey(SoatoData,verbose_name='Код СОАТО')
    kod_okpo = models.CharField('Регистрационный номер респондента (ОКПО)',max_length=12)
    kod_unn= models.IntegerField('Учетный номер плательщика (УНП)')
    kod_gvk = models.IntegerField(' Код респондента по государственного водному кадастру (ГВК)')
    razdel1_fill = models.NullBooleanField(blank=True)
    razdel2_fill = models.NullBooleanField(blank=True)
    razdel3_fill = models.NullBooleanField(blank=True)
    razdel4_fill = models.NullBooleanField(blank=True)

class Part4(models.Model):
    id_part4 = models.AutoField(primary_key=True)
    id_page4 = models.ForeignKey(Page1)
    kod_str4 = models.IntegerField('Код строки')
    value_str = models.CharField(max_length=200)
    value = models.IntegerField()

    #str_401 = models.IntegerField('Численность жителей населенных пунктов, подключенных к централизованной системе водоснабжения, человек: ')
    #str_402 = models.IntegerField('Численность жителей населенных пунктов, подключенных к централизованной системе водоотведения(канализации), человек: ')
    #str_403 = models.IntegerField('Количество дней работы водопользователя')
    #str_404 = models.FloatField('Разрешенные объемы добычи подземной воды, тыс. куб. м/год:')
    #str_405 = models.FloatField('Разрешенные объемы изъятия поверхностной воды, тыс. куб. м/год:')
    #str_406 = models.FloatField('Разрешенные объемы сброса воды в окружающую среду, тыс. куб. м/год:')
    #str_407 = models.FloatField('Разрешенные объемы сброса воды в поверхностные водные объекты, тыс. куб. м/год:')
    #str_408 = models.FloatField('Суммарная проектная мощность водозаборных сооружений для изъятия поверхностной воды, куб.м/сутки:')
    #str_409 = models.FloatField('Суммарная проектная мощность водозаборных сооружений для добычи подземной воды, куб.м/сутки:')
    #str_410 = models.IntegerField('Количество водозаборных сооружений, предназначенных для изъятия поверхностной воды, единиц ')
    #str_411 = models.IntegerField('Количество приборов учета, установленных на водозаборных сооружениях, предназначенных для изъятия поверхностной воды, единиц')
    #str_412 = models.IntegerField('Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - всего, единиц:')
    #str_413 = models.IntegerField('Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - ликвдировано, единиц:')
    #str_414 = models.IntegerField('Количество водозаборных сооружений (скважин), предназначенных для добычи подземной воды - законсервировано, единиц:')
    #str_415 = models.IntegerField('Количество приборов учета, установленных на водозаборных сооружениях, предназначенных для добычи подземной воды, единиц')
    #str_416 = models.IntegerField('Количество приборов учета, установленных на очистных сооружениях, единиц')


class Part1(models.Model):
    id_part1 = models.AutoField(primary_key=True)
    id_page1 = models.ForeignKey(Page1)
    kod_str = models.IntegerField('Код строки')
    source_kod = models.IntegerField('Источник водоснабжения - код')
    naim = models.CharField('Наименование источника', max_length=200)
    location = models.CharField('Местонахождение',max_length=300)
    kod_basin = models.CharField('Код бассейна реки',max_length=10)
    kod_category = models.IntegerField('Код категории качества воды')
    param_1=models.FloatField()
    param_2 = models.FloatField()
    param_3 = models.FloatField()
    kod_wateruser_gvk=models.CharField(' Код водопользователя по государственного водному кадастру (ГВК)',max_length=6)
    use_total=models.FloatField()
    use_tag1 = models.IntegerField()
    vol_tag1 =models.FloatField()
    use_tag2 = models.IntegerField()
    vol_tag2 =models.FloatField()
    use_tag3 = models.IntegerField()
    vol_tag3 =models.FloatField()
    use_tag4 = models.IntegerField()
    vol_tag4 =models.FloatField()
    rash_oborot = models.FloatField()
    vol_oborot = models.FloatField(0)
    trf_cod_wu1=models.IntegerField()
    vol_wu1=models.FloatField()
    trf_cod_wu2=models.IntegerField()
    vol_wu2=models.FloatField()
    trf_cod_wu3=models.IntegerField()
    vol_wu3=models.FloatField()
    trf_cod_au=models.IntegerField()
    vol_au=models.FloatField()
    code_gvk_au=models.CharField(' Код водопользователя по государственного водному кадастру (ГВК)',max_length=6)
    lost_total= models.FloatField()
    lost_transport = models.FloatField()
    use_bez = models.FloatField()


class Part2(models.Model):
    id_part2 = models.AutoField(primary_key=True)
    id_page2 = models.ForeignKey(Page1)
    kod_str2 = models.IntegerField('Код строки')
    outlet_kod = models.IntegerField('Источник водоприемника - код')
    naim = models.CharField('Наименование источника', max_length=200)
    location = models.CharField('Местонахождение',max_length=300)
    kod_basin2 = models.CharField('Код бассейна реки',max_length=10)
    kod_category2 = models.IntegerField('Код категории качества воды')
    sbros=models.FloatField()
    pribor_sbros = models.FloatField()
    sbros_without = models.FloatField()
    sbros_nogood = models.FloatField()
    sbros_norm = models.FloatField()
    kod_wwtp=models.CharField(' Код очистных',max_length=6)    #  check legth
    wwtp_project=models.FloatField()
    filtration_fields = models.FloatField()

class Part3(models.Model):
    id_part3 = models.AutoField(primary_key=True)
    id_page3 = models.ForeignKey(Page1)
    kod_str3 = models.IntegerField('Код строки')
    location_outlet = models.CharField('Местонахождение',max_length=300)
    bod5=models.FloatField()
    cod=models.FloatField()
    ssolids=models.FloatField()
    mineral = models.FloatField()
    sulphate = models.FloatField()
    chloride = models.FloatField()
    phosp_ion = models.FloatField()
    totalp=models.FloatField()
    nh4=models.FloatField()
    no2=models.FloatField()
    no3=models.FloatField()
    detergents = models.FloatField()
    oil_p = models.FloatField()
    fe_tot = models.FloatField()
    cr_tot = models.FloatField()
    ni = models.FloatField()
    cu = models.FloatField()
    lead = models.FloatField()
    mercury = models.FloatField()
    zink = models.FloatField()

class TestItem(models.Model):
    id_testitem= models.AutoField(primary_key=True)
    name = models.CharField(20,max_length=30)
    code = models.IntegerField()
