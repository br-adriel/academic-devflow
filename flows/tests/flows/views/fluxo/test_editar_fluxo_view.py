from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve
from flows.models import Fluxo
from flows.views import editar_fluxo_view

class EditarFluxoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo teste", descricao="Descrição teste")
        self.targetUrl = reverse_lazy('flows:editar_fluxo', kwargs={'pk': self.fluxo_obj.id})

    def test_editar_fluxo(self):
        """Verifica se os dados foram de fato alterados"""

        data = {
            'nome': "Fluxo novo",
            'descricao': "Descrição nova"
        }

        self.client.post(self.targetUrl, data)
        fluxo_atualizado = Fluxo.objects.get(id=self.fluxo_obj.id)
        self.assertEqual(fluxo_atualizado.nome, 'Fluxo novo')
        self.assertEqual(fluxo_atualizado.descricao, 'Descrição nova')

    def test_if_url_is_linked_to_view(self):
        """Verifica se a url está vinculada a view"""
        found = resolve(self.targetUrl)
        self.assertEqual(found.func, editar_fluxo_view)

    def test_editing_for_a_non_existing_object(self):
        """Verifica como o sistema se comporta quando a url contém um id não existente"""
        url = reverse_lazy('flows:editar_fluxo', kwargs={'pk': 100})

        data = {
            'nome': "Fluxo novo",
            'descricao': "Descrição nova"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 404)

    def test_editing_by_sending_invalid_data(self):
        """Verifica como o sistema se comporta quando é enviado uma instância incorreta"""
        data = {
            'name': "Fluxo errado",
            'description': "Descrição errada"
        }

        self.client.post(self.targetUrl, data)
        fluxo_atualizado = Fluxo.objects.get(id=self.fluxo_obj.id)
        self.assertNotEqual(fluxo_atualizado.nome, 'Fluxo errado')
        self.assertNotEqual(fluxo_atualizado.nome, 'Descrição errada')
        

