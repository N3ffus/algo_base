from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('algorithms/<int:id>/practice', views.algorithm_practice, name='algorithm_practice'),
    path('algorithms/<int:id>/theory', views.algorithm_theory, name='algorithm_theory'),
    path('algorithms/<int:id>', views.algorithm, name='algorithm'),
    path('algorithms', views.algorithms, name='algorithms'),
    path('data_structures/<int:id>/practice', views.data_structure_practice, name='data_structure_practice'),
    path('data_structures/<int:id>/theory', views.data_structure_theory, name='data_structure_theory'),
    path('data_structures/<int:id>', views.data_structure, name='data_structure'),
    path('data_structures', views.data_structures, name='data_structures'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete')
]