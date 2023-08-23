from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    title = '''home page'''
    return render(request,'index.html',{"title":title})