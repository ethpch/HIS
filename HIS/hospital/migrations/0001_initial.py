# Generated by Django 3.0.7 on 2020-06-29 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HISOperator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkitem',
            fields=[
                ('id', models.AutoField(default=4, max_length=10, primary_key=True, serialize=False, verbose_name='检查项目ID')),
                ('itemname', models.CharField(max_length=30, unique=True, verbose_name='检查项目名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='检查项目价格')),
            ],
            options={
                'verbose_name': '检查项目',
                'verbose_name_plural': '检查项目',
            },
        ),
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.AutoField(default=6, max_length=10, primary_key=True, serialize=False, verbose_name='科室ID')),
                ('deptname', models.CharField(max_length=20, unique=True, verbose_name='科室名称')),
            ],
            options={
                'verbose_name': '挂号科室',
                'verbose_name_plural': '挂号科室',
            },
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(default=10, max_length=10, primary_key=True, serialize=False, verbose_name='医生ID')),
                ('dname', models.CharField(max_length=20, unique=True, verbose_name='医生名称')),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.dept', verbose_name='科室')),
            ],
            options={
                'verbose_name': '医生',
                'verbose_name_plural': '医生',
            },
        ),
        migrations.CreateModel(
            name='inspectitem',
            fields=[
                ('id', models.AutoField(default=3, max_length=10, primary_key=True, serialize=False, verbose_name='检验项目ID')),
                ('inspectname', models.CharField(max_length=30, unique=True, verbose_name='检验项目名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='检验项目价格')),
            ],
            options={
                'verbose_name': '检验项目',
                'verbose_name_plural': '检验项目',
            },
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(default=3, max_length=10, primary_key=True, serialize=False, verbose_name='级别ID')),
                ('levelname', models.CharField(max_length=20, unique=True, verbose_name='级别名称')),
                ('cost', models.IntegerField(max_length=5, verbose_name='级别花费')),
            ],
            options={
                'verbose_name': '挂号级别',
                'verbose_name_plural': '挂号级别',
            },
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('pid', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='患者ID')),
                ('pname', models.CharField(max_length=20, verbose_name='患者名称')),
                ('sex', models.CharField(max_length=10, verbose_name='患者性别')),
                ('age', models.IntegerField(blank=True, max_length=3, null=True, verbose_name='患者年龄')),
                ('birthday', models.CharField(blank=True, max_length=10, verbose_name='患者生日')),
                ('idcard', models.CharField(max_length=20, unique=True, verbose_name='患者身份证')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='患者地址')),
                ('createdate', models.DateField(verbose_name='创建日期')),
                ('cost', models.IntegerField(max_length=5, verbose_name='患者花费')),
                ('pstatus', models.CharField(max_length=10, verbose_name='患者就诊状态')),
                ('status', models.IntegerField(max_length=2, verbose_name='患者状态')),
                ('operatedate', models.DateField(auto_now=True, verbose_name='操作日期')),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.dept', verbose_name='科室')),
                ('doctorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor', verbose_name='医生')),
                ('levelid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.level', verbose_name='级别')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HISOperator.User', verbose_name='操作人')),
            ],
            options={
                'verbose_name': '患者',
                'verbose_name_plural': '患者',
            },
        ),
        migrations.CreateModel(
            name='medicalrecord',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='病例ID')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='主诉')),
                ('medicalhistory', models.CharField(blank=True, max_length=100, verbose_name='疾病史')),
                ('familyhistory', models.CharField(blank=True, max_length=100, verbose_name='家族病史')),
                ('initialresult', models.CharField(max_length=100, verbose_name='初步诊断')),
                ('result', models.CharField(blank=True, max_length=100, verbose_name='检验结果')),
                ('finalresult', models.CharField(blank=True, max_length=100, verbose_name='最终诊断')),
                ('status', models.IntegerField(max_length=2, verbose_name='状态')),
                ('operatedate', models.DateField(auto_now=True, verbose_name='操作日期')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HISOperator.User', verbose_name='操作人')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient', verbose_name='患者')),
            ],
            options={
                'verbose_name': '病例',
                'verbose_name_plural': '病例',
            },
        ),
        migrations.CreateModel(
            name='inspectitemrecord',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='检验申请ID')),
                ('amount', models.IntegerField(max_length=2, verbose_name='检验申请次数')),
                ('paystatus', models.IntegerField(max_length=2, verbose_name='检验申请缴费状态')),
                ('inspectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.inspectitem', verbose_name='检验项目')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient', verbose_name='患者')),
            ],
            options={
                'verbose_name': '检验申请记录',
                'verbose_name_plural': '检验申请记录',
            },
        ),
        migrations.CreateModel(
            name='checkitemrecord',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False, verbose_name='检查申请ID')),
                ('amount', models.IntegerField(max_length=2, verbose_name='检查申请次数')),
                ('paystatus', models.IntegerField(max_length=2, verbose_name='检查申请缴费状态')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.checkitem', verbose_name='检查项目')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient', verbose_name='患者')),
            ],
            options={
                'verbose_name': '检查申请记录',
                'verbose_name_plural': '检查申请记录',
            },
        ),
    ]