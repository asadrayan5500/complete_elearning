from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def courses(request):
    return render(request, 'courses.html')
def team(request):
    return render(request, 'team.html')
def contact(request):
    return render(request, 'contact.html')