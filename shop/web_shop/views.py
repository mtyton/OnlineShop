from django.shortcuts import render
from django.views import View

from web_shop.models import Promotion


class HomeView(View):

    template_name = "web_shop/index.html"

    def get_context_data(self) -> dict:
        return {
            'promotions': Promotion.objects.get_latest_promotions()
        }

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
