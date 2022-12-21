from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve
from flows.models import Fluxo, Etapa

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

    def test_deletion_when_request_is_not_post(self):
        """Verifica como o sistema se comporta quando o método da requisição é diferente de POST"""

        self.client.delete(self.targetUrl)
        quant_flows = Fluxo.objects.count()
        self.assertEqual(quant_flows, 1)

    def test_the_context_of_the_response(self):
        """Verifica se existem fluxos no contexto da response"""

        response = self.client.delete(self.targetUrl)
        self.assertTrue('flow' in response.context)

    def test_the_deletion_of_the_flow_with_registered_steps(self):
        """Verifica como o sistema se comporta quando existem etapas vinculadas ao fluxo"""

        self.etapa_iniciada = Etapa.objects.create(
            nome="Etapa teste",
            descricao="Descrição teste",
            numero='1',
            data_inicio='2022-12-01',
            data_finalizacao='2022-12-31',
            gameficada=True,
            fluxo = self.fluxo_obj
        )

        self.client.post(self.targetUrl)
        quant_flows = Fluxo.objects.count()
        self.assertEqual(quant_flows, 1)