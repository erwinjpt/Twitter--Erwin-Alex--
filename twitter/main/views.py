from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from main.models import Tweet 
from main.forms import TweetForm
from main.forms import UserCreationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.models import User


def home(request):
    return render_to_response('home.html',{

	})

def add_tweet(request):
	form = TweetForm()
	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('add_tweet.html',{
		'form': form,
	}, RequestContext(request))

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render_to_response('register.html',{
		'form': form,
	}, RequestContext(request))

def login(request):
	return render_to_response('login.html',
		{},
		RequestContext(request))

def login_process(request):
	user = authenticate(username = request.POST['user'],
			password = request.POST['password'])
	if user is not None:
		return render_to_response('home.html',{
			'mensaje_login' : 'Usuario y password correctos',
			},RequestContext(request)) 
	else:
		return render_to_response('login.html',{
			'mensaje_login' : 'Ingrese el usuario y clave correctamente',
		},RequestContext(request))

def delete_tweet(request, pk):
	tweet = get_object_or_404(Tweet,pk=pk)
	tweet.delete()
	Tweet.objects.filter(pk=pk).delete()
	return redirect('home')

