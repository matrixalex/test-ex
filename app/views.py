from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template.context_processors import csrf
from django.views.generic import TemplateView
from django.contrib import auth
# Create your views here.

def index(request):
    args = {}
    args.update(csrf(request))
    args['user'] = request.user
    args['logged'] = request.user.is_authenticated
    args['request'] = request
    #print( '\n\n\n'+str(args['user'])+'  ' + str(args['logged']) + '\n\n\n')
    return render(
        request,
        'app/index.html',
        args
    )
