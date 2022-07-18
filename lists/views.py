from django.views.generic import ListView

from .models import List

# Create your views here.

class ListsListView(ListView):
    model = List
    template_name = 'lists.html'