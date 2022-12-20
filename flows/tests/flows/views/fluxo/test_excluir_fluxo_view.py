from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve
from flows.models import Fluxo

class ExcluirFluxoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo teste", descricao="Descrição teste")
        self.targetUrl = reverse_lazy('flows:excluir_fluxo', kwargs={'pk': self.fluxo_obj.id})
    
    def test_excluir_fluxo(self):
        """Verifica se o fluxo é excluído, caso não haja etapas cadastradas no fluxo"""

        self.client.post(self.targetUrl)
        quant_flows = Fluxo.objects.count()
        self.assertEqual(quant_flows, 0)
