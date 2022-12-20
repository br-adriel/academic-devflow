from django.urls import path
from .views import pagina_inicial_view, adicionar_fluxo_view, detalhes_fluxo_view, editar_fluxo_view, adicionar_etapa_view, editar_etapa_view, excluir_etapa_view

app_name = 'flows'

urlpatterns = [
    path('', pagina_inicial_view, name='inicio'),
    path('adicionar', adicionar_fluxo_view, name='adicionar_fluxo'),
    path('<int:pk>', detalhes_fluxo_view, name='detalhes_fluxo'),
    path('<int:pk>', editar_fluxo_view, name='editar_fluxo'),
    path('<int:fluxo_pk>/adicionar', adicionar_etapa_view, name='adicionar_etapa'),
    path('<int:fluxo_pk>/editar/<int:pk>',
         editar_etapa_view, name='editar_etapa'),
    path('<int:fluxo_pk>/excluir/<int:pk>',
         excluir_etapa_view, name='excluir_etapa'),
]
