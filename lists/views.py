from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect

from .models import List, Entry, AddEntryForm

# Create your views here.

class ListsListView(ListView):
    model = List
    template_name = 'lists.html'

class DeleteEntryView(DeleteView):
    model = Entry
    success_url = reverse_lazy('lists')

class AddEntryView(CreateView):
    model = Entry
    form_class = AddEntryForm
    success_url = reverse_lazy('lists')

class AddListView(CreateView):
    model = List
    fields = ('name', 'repeats',)
    template_name = 'add-list.html'
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DeleteListView(DeleteView):
    model = List
    success_url = reverse_lazy('lists')