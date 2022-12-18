from django.urls import path
from .views import pagina_inicial_view, adicionar_fluxo_view, detalhes_fluxo_view

app_name = 'flows'

urlpatterns = [
    path('', pagina_inicial_view, name='inicio'),
    path('adicionar', adicionar_fluxo_view, name='adicionar'),
    path('<int:pk>', detalhes_fluxo_view, name='detalhes'),
]
