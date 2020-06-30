from django.db import models

# Create your models here.


class patient(models.Model):
    pid = models.AutoField('患者ID', max_length=10, primary_key=True)
    pname = models.CharField('患者名称', max_length=20)
    sex = models.CharField('患者性别', max_length=10)
    age = models.IntegerField('患者年龄', max_length=3, blank=True, null=True)
    birthday = models.CharField('患者生日', max_length=10, blank=True)
    idcard = models.CharField('患者身份证', max_length=20, unique=True)
    address = models.CharField('患者地址', max_length=100, blank=True)
    levelid = models.ForeignKey('hospital.level', on_delete=models.CASCADE, verbose_name='级别')
    deptid = models.ForeignKey('hospital.dept', on_delete=models.CASCADE, verbose_name='科室')
    doctorid = models.ForeignKey('hospital.doctor', on_delete=models.CASCADE, verbose_name='医生')
    createdate = models.DateField('创建日期')
    cost = models.IntegerField('患者花费', max_length=5)
    pstatus = models.CharField('患者就诊状态', max_length=10)
    status = models.IntegerField('患者状态', max_length=2)
    operator = models.ForeignKey('HISOperator.User', on_delete=models.CASCADE, verbose_name='操作人')
    operatedate = models.DateField('操作日期', auto_now=True)

    def __str__(self):
        return self.pname

    class Meta:
        verbose_name = '患者'
        verbose_name_plural = '患者'

class level(models.Model):
    id = models.AutoField('级别ID', max_length=10, primary_key=True, default=3)
    levelname = models.CharField('级别名称', max_length=20, unique=True)
    cost = models.IntegerField('级别花费', max_length=5)

    def __str__(self):
        return self.levelname

    class Meta:
        verbose_name = '挂号级别'
        verbose_name_plural = '挂号级别'

class dept(models.Model):
    id = models.AutoField('科室ID', max_length=10, primary_key=True, default=6)
    deptname = models.CharField('科室名称', max_length=20, unique=True)

    def __str__(self):
        return self.deptname

    class Meta:
        verbose_name = '挂号科室'
        verbose_name_plural = '挂号科室'

class doctor(models.Model):
    id = models.AutoField('医生ID', max_length=10, primary_key=True, default=10)
    dname = models.CharField('医生名称', max_length=20, unique=True)
    deptid = models.ForeignKey('hospital.dept', on_delete=models.CASCADE, verbose_name='科室')

    def __str__(self):
        return self.dname

    class Meta:
        verbose_name = '医生'
        verbose_name_plural = '医生'

class medicalrecord(models.Model):
    id = models.AutoField('病例ID', max_length=10, primary_key=True)
    pid = models.ForeignKey('hospital.patient', on_delete=models.CASCADE, verbose_name='患者')
    description = models.CharField('主诉', max_length=100, blank=True)
    medicalhistory = models.CharField('疾病史', max_length=100, blank=True)
    familyhistory = models.CharField('家族病史', max_length=100, blank=True)
    initialresult = models.CharField('初步诊断', max_length=100)
    result = models.CharField('检验结果', max_length=100, blank=True)
    finalresult = models.CharField('最终诊断', max_length=100, blank=True)
    status = models.IntegerField('状态', max_length=2)
    operator = models.ForeignKey('HISOperator.User', on_delete=models.CASCADE, verbose_name='操作人')
    operatedate = models.DateField('操作日期', auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '病例'
        verbose_name_plural = '病例'

class checkitem(models.Model):
    id = models.AutoField('检查项目ID', max_length=10, primary_key=True, default=4)
    itemname = models.CharField('检查项目名称', max_length=30, unique=True)
    price = models.DecimalField('检查项目价格', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.itemname

    class Meta:
        verbose_name = '检查项目'
        verbose_name_plural = '检查项目'

class checkitemrecord(models.Model):
    id = models.AutoField('检查申请ID', max_length=10, primary_key=True)
    pid = models.ForeignKey('hospital.patient', on_delete=models.CASCADE, verbose_name='患者')
    cid = models.ForeignKey('hospital.checkitem', on_delete=models.CASCADE, verbose_name='检查项目')
    amount = models.IntegerField('检查申请次数', max_length=2)
    paystatus = models.IntegerField('检查申请缴费状态', max_length=2)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '检查申请记录'
        verbose_name_plural = '检查申请记录'

class inspectitem(models.Model):
    id = models.AutoField('检验项目ID', max_length=10, primary_key=True, default=3)
    inspectname = models.CharField('检验项目名称', max_length=30, unique=True)
    price = models.DecimalField('检验项目价格', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.inspectname

    class Meta:
        verbose_name = '检验项目'
        verbose_name_plural = '检验项目'

class inspectitemrecord(models.Model):
    id = models.AutoField('检验申请ID', max_length=10, primary_key=True)
    pid = models.ForeignKey('hospital.patient', on_delete=models.CASCADE, verbose_name='患者')
    inspectid = models.ForeignKey('hospital.inspectitem', on_delete=models.CASCADE, verbose_name='检验项目')
    amount = models.IntegerField('检验申请次数', max_length=2)
    paystatus = models.IntegerField('检验申请缴费状态', max_length=2)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '检验申请记录'
        verbose_name_plural = '检验申请记录'