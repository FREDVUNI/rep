from django.shortcuts import render
def index(request):
	context={}
	return render(request,"divinehearts/index.html",context)

def enroll(request):
	context={}
	return render(request,"divinehearts/enroll.html",context)

def about(request):
	context={}
	return render(request,"divinehearts/about.html",context)

def services(request):
	context={}
	return render(request,"divinehearts/services.html",context)

def events(request):
	context={}
	return render(request,"divinehearts/events.html",context)

def gallery(request):
	context={}
	return render(request,"divinehearts/gallery.html",context)

def contact(request):
	context={}
	return render(request,"divinehearts/contact.html",context)

