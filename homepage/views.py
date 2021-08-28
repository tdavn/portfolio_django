from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ContactMessage

# Create your views here.

class HompageView(TemplateView):
    '''Display homepage'''
    template_name = 'homepage/index.html'

    def post(self, request):
        info = self.request.POST
        ContactMessage.objects.create(
        name = info['name'],
        email = info['email'],
        message = info['message']
        )
        context = {
        'temp_mes': 'Your message has been recored. Thank you!',
        }
        return render(request, self.template_name, context)


class PortfolioView(TemplateView):
    '''Display portfolio page'''
    template_name = 'homepage/portfolio.html'


class Ing4View(TemplateView):
    '''Display portfolio page of Ing4 project'''
    template_name = 'homepage/ing4.html'


class NanobodyView(TemplateView):
    '''Display portfolio page of Nanobody project'''
    template_name = 'homepage/nanobody.html'


class TrichostatinView(TemplateView):
    '''Display portfolio page of TSA project'''
    template_name = 'homepage/trichostatin.html'


class NetosisView(TemplateView):
    '''Display portfolio page of Netosis project'''
    template_name = 'homepage/netosis.html'


class Ggtpase3View(TemplateView):
    '''Display portfolio page of YKT6 project'''
    template_name = 'homepage/ggtpase3.html'


class RalgapView(TemplateView):
    '''Display portfolio page of Ral GaP protein project'''
    template_name = 'homepage/ralgap.html'

