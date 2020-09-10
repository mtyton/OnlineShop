from django.shortcuts import render
from django.views import View
from web_shop.models import CarouselData


class HomeView(View):
    def get(self, request):
        images = CarouselData.get_latest_images()
        context = {
            'img_0': images[0].image,
            'img_1': images[1].image,
            'img_2': images[2].image,
        }
        return render(request, 'web_shop/index.html', context=context)