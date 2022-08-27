from django.urls import path

from aplicatia3 import views

app_name = 'job'

urlpatterns = [
    path('', views.JobView.as_view(), name='lista_job'),
    path('adaugare/', views.CreateJobView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateJobView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.delete_job, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_job, name='activeaza'),
]