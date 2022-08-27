from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Locations, nume_orase
import pandas as pd


class LocationsView(LoginRequiredMixin, ListView):
    model = Locations
    template_name = 'aplicatie1/locations_index.html'
    paginate_by = 5


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Locations
    fields = ['country','city']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Locations
    fields = ['country','city']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


def load_cities(request):
    country_id = request.GET.get('country')
    df = pd.read_csv("C:/Users/radul/OneDrive/Desktop/GooglePython/proiect/worldcities.csv")
    sortare2 = (df['city_ascii'])
    df_list = sortare2[df['country'].str.contains(country_id)]
    list2 = []
    for x in df_list:
        list2.append((x, x))
    list2 = sorted(list2)
    cities = tuple(list2)
    return render(request,'aplicatie1/city_dropdown_list_options.html',{'cities': cities})


@login_required
def delete_location(request, pk):
    Locations.objects.filter(id=pk).update(active=0)
    return redirect('locations:lista_locatii')


@login_required
def activate_location(request, pk):
    Locations.objects.filter(id=pk).update(active=1)
    return redirect('locations:lista_locatii')