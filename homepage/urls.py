from django.urls import path
from .views import HompageView, PortfolioView, NanobodyView
from .views import TrichostatinView, NetosisView, Ing4View, Ggtpase3View, RalgapView

app_name = 'homepage'

urlpatterns = [
    path('', HompageView.as_view(), name='home_id'),
    path('portfolio', PortfolioView.as_view(), name='portfolio1'),
    path('portfolio/ing4', Ing4View.as_view(), name='ing4'),
    path('portfolio/nanobody', NanobodyView.as_view(), name='nanobody'),
    path('portfolio/trichostatin', TrichostatinView.as_view(), name='trichostatin'),
    path('portfolio/netosis', NetosisView.as_view(), name='netosis'),
    path('portfolio/ggtpase3', Ggtpase3View.as_view(), name='ggtpase3'),
    path('portfolio/ralgap', RalgapView.as_view(), name='ralgap'),
]
