from django.shortcuts import render
from django.views import View

from ..core.mixins import AnonymousUserMixin


class IndexView(AnonymousUserMixin, View):
    def get(self, request):
        return render(request, 'www/index.html', self.get_context_data(request))

    def get_context_data(self, request):
        context = super().get_anonymous_data(request)
        return context