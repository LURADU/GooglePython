from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatia3.models import Job


class JobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'aplicatie3/job_index.html'
    paginate_by = 5


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'aplicatie3/job_form.html'

    def get_success_url(self):
        return reverse('job:lista_job')


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['type','url','title','description','how_to_apply']
    template_name = 'aplicatie3/job_form.html'

    def get_success_url(self):
        return reverse('job:lista_job')


@login_required
def delete_job(request, pk):
    Job.objects.filter(id=pk).update(active=0)
    return redirect('job:lista_job')


@login_required
def activate_job(request, pk):
    Job.objects.filter(id=pk).update(active=1)
    return redirect('job:lista_job')