from django.db import models

#   python manage.py makemigrations    生成迁移脚本
#   python manage.py   migrate   插入数据库中
#用户表
class  Users(models.Model):
    username=models.CharField(max_length=100) #用户名
    password=models.CharField(max_length=200) #密码
    sex=models.SmallIntegerField()   #性别
    age=models.BigIntegerField()  #年龄
    logintime=models.DateTimeField() #最后登录日期

    class Meta:
        db_table='users'
#公告表
class  Notice(models.Model):
     title=models.CharField(max_length=300) #标题
     content=models.CharField(max_length=500) #内容
     date=models.DateTimeField()#发布日期
     state=models.SmallIntegerField()#状态
     User=models.ForeignKey('Users',models.CASCADE,null=False)#发布人 管理管理员表
     color=models.CharField(max_length=100,null=False,default='layui-bg-red')#公告颜色
     class Meta:
         db_table='Notice'