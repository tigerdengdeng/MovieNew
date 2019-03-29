from django.urls import path,include
from. import  views

urlpatterns=[
    path("login/",views.login,name='login'), #name='login' 相当于给url取名 跳转反转时作为标识
    path("save/",views.savelogin,name='savelogin'),  #登录函数
    path("Home/", views.Index, name='Index'), # 首页
    path("Info/", views.Indexinfo, name='Indexinfo'),# 首页显示信息
    path("UserList/",views.IUsers, name='IUsers'),  # 用户信息
    path("IuserInfo/", views.IUserInfo, name='IUserInfo'),  # 加载列表用户信息
]
