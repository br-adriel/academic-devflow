from django.urls import path
from artifacts.views import create_artifact_view, artifact_list, home_artifact, update_artifact, delete_artifact

app_name = 'artifacts'

urlpatterns = [
    path('', home_artifact, name='home'),
    path('registrar/', create_artifact_view, name='registrar'),
    path('listar/', artifact_list, name='listar'),
    path('listar/<int:pk>/editar', update_artifact, name='update_artifact'),
    path('listar/<int:pk>/excluir', delete_artifact, name='delete_artifact')
]
