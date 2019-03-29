from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from django.http.request import HttpRequest
from .models import Users,Notice #引用模型
from  django.http import  JsonResponse #Json操作
from django.core import serializers
import json
from  django.forms.models import model_to_dict
#登录页面
def login(request):
    # 检测cookies是否存在
    login_username = request.session.get('username')
    if login_username:
        #session 失效时间10s
        # request.session.set_expiry(10)
        # 获取登录用户信息
        login_user = Users.objects.get(username=login_username)
        # 返回登录成功后页面
        return redirect('/Home/')
    else:
        # 进入未登录状态的主页
        return render(request,'login/login.html')

#登录提交
def savelogin(request):
    # 接受数据
   if request.method=='GET':
       return  render(request,'login/login.html')
   else:
      username = request.POST.get("username")
      password = request.POST.get("password")
      checkmy =request.POST.get("check")
      user=Users.objects.filter(username=username,password=password).first()
      if user:
          if checkmy=='true':
              # c存入session
              request.session['username'] = username
              print(request.session.get('username'))
          return  JsonResponse({'code':200})
      else:
           return JsonResponse({"code":500})

#首页
def  Index(request):
    Noticeitem=Notice.objects.filter(state=1) #查询公告
    return  render(request,'Home/index.html',context={'Noticeitem':Noticeitem})

# 首页加载第一页
def Indexinfo(request):
    return  render(request,'Home/welcome.html')

#用户管理页面
def  IUsers(request):
     return  render(request,'Users/UserList.html')

#加载用户列表数据
def IUserInfo(request):
    page=request.GET.get('page')
    rows=request.GET.get('limit')
    i=(int(page)-1)*int(rows)
    j=(int(page)-1)*int(rows)+int(rows)

    useritem = Users.objects.all()
    total = useritem.count()
    useritem=useritem[i:j]

    resultdict = {} #字典
    resultdict['total'] = total
    dice=[] #集合
    for p in useritem:

        dic=model_to_dict(p)
        dice.append(dic)
    resultdict['code'] = 0
    resultdict['msg'] = ""
    resultdict['count'] = total
    resultdict['data'] = dice

    return JsonResponse(resultdict, safe=False)
    # return render(request, "login.html", {'username': json.dumps(username)}