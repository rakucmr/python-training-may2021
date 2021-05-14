from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET

from .forms import UniversityForm
from .models import University


@require_GET
def index(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, 'university/index.html', context)


@require_GET
def university_details(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    context = {'university': university}
    return render(request, 'university/university_details.html', context)


@require_http_methods(["GET", "POST"])
def university_update(request, university_id):
    university = get_object_or_404(University, pk=university_id)

    if request.method == 'POST':
        form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('university_details', args=(university.id,)))

    else:
        form = UniversityForm(instance=university)

    context = {'university': university, 'form': form}
    return render(request, 'university/university_update.html', context)
