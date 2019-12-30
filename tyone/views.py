from django.shortcuts import render,HttpResponse
def home(request):
	context={}
	return HttpResponse("hello word")
# def about(request):
# 	context={}
# 	template='about.html'
# 	return render(request,template,context)