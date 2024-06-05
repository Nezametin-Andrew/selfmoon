from django.shortcuts import render
from django.views import View


class BalanceView(View):

    def get(self, request):
        return render(request=request, template_name='account/balance.html', context={})
