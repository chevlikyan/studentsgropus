from django.shortcuts import render
from django.views.generic import ListView, DetailView
from studentsandgroups.models import Group, Student


# Create your views here.
class StudentListView(ListView):
    template_name = 'home.html'
    queryset = Student.objects.all()
    context_object_name = 'Student'
    # paginate_by = 2
    ordering = ['name']


class GroupDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group_detail'
