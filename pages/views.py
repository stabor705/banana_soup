from django.views.generic import TemplateView
from django.contrib.auth import get_user
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request):
        user = get_user(request)
        if not user.is_anonymous:
            return HttpResponseRedirect(reverse('lists'))
        return super().dispatch(request)