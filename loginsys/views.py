from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.
def log(request):
    return render(request,"loginsys/login.html")
def registr(request):
    return render(request, "loginsys/registration.html")

def logt(request):
    auth.logout(request)
    return redirect('../../')

@csrf_exempt
def login(request):
    args = {}
    args.update(csrf(request))
    #print('\n\nЗашли в логин\n\n')
    if request.POST:
        #print('\n\nЗашли в пост\n\n')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user != None:
            #print('\n\nЮзер найден\n\n')
            user.is_authentificated = True
            auth.login(request,user)
            args['user'] = request.user

            #print(args['user'])
            return redirect('../../',context=args)
        else:
            #print('\n\nНет юзера\n\n')
            args['error'] = 'Что-то не так'
            return render_to_response('loginsys/login.html',args)
    else: return render_to_response('loginsys/login.html',args)
@csrf_exempt
def registration(request):
    args = {}
    args.update(csrf(request))
    # print('\n\nЗашли в логин\n\n')
    if request.POST:
        # print('\n\nЗашли в пост\n\n')
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        allNames = [user.username for user in User.objects.all()]
        pas2 = request.POST['pass2']
        if password != pas2 or username == '' or username in allNames:
            args['error'] = 'Что-то не так'
            return render_to_response('loginsys/registration.html',context=args)
            # print('\n\nЮзер найден\n\n')

            # print(args['user'])

        else:
            try:
                is_staff = True if request.POST['is_staff'] == 'on' else False
            except:
                is_staff = False
            user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password, is_staff = is_staff)
            auth.login(request,user)
            user.save()
            return redirect('../../',context=args)
    else:
        return render_to_response('loginsys/registration.html',context=args)