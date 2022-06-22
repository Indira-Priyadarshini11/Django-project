from django.shortcuts import render

def music(request):
    return render(request,'music.html')
def dance(request):
    return render(request,'dance.html')
def home(request):
    return render(request,'home.html')
