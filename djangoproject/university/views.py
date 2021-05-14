from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import DetailView, ListView, UpdateView

from .forms import UniversityForm
from .models import University


class UniversityListView(ListView):
    model = University
    context_object_name = 'universities'


class UniversityDetailView(DetailView):
    model = University
    context_object_name = 'university'


class UniversityUpdateView(LoginRequiredMixin, UpdateView):
    model = University
    fields = ['name', 'city', 'description']


@require_GET
def index(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, 'university/university_list.html', context)


@require_GET
def university_details(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    context = {'university': university}
    return render(request, 'university/university_detail.html', context)


@require_http_methods(["GET", "POST"])
@login_required
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
    return render(request, 'university/university_form.html', context)
