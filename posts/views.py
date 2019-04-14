from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from django.template.context_processors import csrf
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from .models import Post,PostInfo
from django.contrib import auth
# Create your views here.
def show(request):
    return HttpResponse("No posts")

def showAll(request):
    print(request.user.is_authenticated)
    return render(request,'posts/wrapper.html',context={'posts':Post.objects.all(),'request':request})

def showPost(request,pk):
    args = {}
    args['post'] = get_object_or_404(Post,pk=pk)
    args['user'] = auth.get_user(request) 
    #print('\n\n\n'+str(args['user'])+'\n\n\n')
    return render(request,'posts/post.html',args)

def editPost(request,pk):
    args = {}
    args['post'] = get_object_or_404(Post, pk=pk)
    args['pk'] = pk
    args['user'] = request.user
    return render(request,'posts/edit-post.html',args)
@csrf_exempt
def edit(request):
    args = {}
    args.update(csrf(request))
    #print('\n\nЗашли в edit\n\n')
    if request.POST:
        # print('\n\nЗашли в пост\n\n')
        title = request.POST['title']
        text = request.POST['text']
        if title == '':
            args['error'] = 'Ошибка'
            args['post'] = get_object_or_404(Post,pk=request.POST['id'])
            return render_to_response('posts/edit-post.html', context=args)
        post = get_object_or_404(Post,pk=request.POST['id'])
        post.title = title
        post.text = text
        post.save()
        #print("\n\n\n\n\n OFOFOF \n\n\n\n")
        return showAll(request)
    else:
        return render_to_response('posts/edit-post.html', context=args)



def createPost(request):
    args = {}
    args['user'] = request.user
    args['request'] = request
    return render(request,'posts/create-post.html',args)
@csrf_exempt
def create(request):
    args = {}
    args.update(csrf(request))
    #print('\n\nЗашли в edit\n\n')
    if request.POST:
        # print('\n\nЗашли в пост\n\n')
        title = request.POST['title']
        text = request.POST['text']
        if title == '':
            args['error'] = 'Ошибка'
            args['user'] = request.user
            return render_to_response('posts/create-post.html',context=args)
        post = Post.objects.create(author = request.POST['author'], title = title, text = text, date=datetime.datetime.now())
        post.save()
        #print("\n\n\n\n\n OFOFOF \n\n\n\n")
        return showAll(request)
    else: return render_to_response('posts/create-post.html',context=args)