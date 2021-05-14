from django.shortcuts import render

from .models import University


def index(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, 'university/index.html', context)
