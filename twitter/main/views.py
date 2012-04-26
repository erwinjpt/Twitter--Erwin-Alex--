from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from main.models import Tweet 
from main.forms import TweetForm
from main.forms import UserCreationForm


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

def delete_tweet(request, pk):
	tweet = get_object_or_404(Tweet,pk=pk)
	tweet.delete()
	Tweet.objects.filter(pk=pk).delete()
	return redirect('home')
