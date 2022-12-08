from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse
from artifacts.models import Artefato
from projects.models import Projeto


class CreateArtifactView(TestCase):
    def setUp(self):
        self.client = Client()
        self.targetUrl = reverse_lazy('artifacts:registrar')
        self.projeto = Projeto.objects.create(
            nome="Projeto teste", data_inicio='2022-01-01', data_termino='2022-12-31', situacao="Iniciado")
        self.test_values = {
            "nome": "Modelo de dados",
            "descricao": "Modelo de dados conceitual",
            "data_entrega": "2023-01-01",
            "situacao": "Em andamento",
            "projeto": self.projeto.id
        }

    def test_get_request_retorna_form(self):
        """Verifica se a view exibe o formulário de criacao de artefato em request get"""

        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(
            response.context, "Não foi usado contexto na renderização")
        self.assertIsNotNone(response.context.get('form'), "'form' não existe")

    def test_post_request_todos_campos_cria_objeto(self):
        """Verifica se a view cria um Artefato quando todos os campos são passados em request post"""

        initial_count = Artefato.objects.count()
        self.client.post(self.targetUrl, self.test_values)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_request_campos_obrigatorios_cria_objeto(self):
        """Verifica se a view cria um Artefato quando os campos obrigatórios são passados em request post"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "data_entrega": self.test_values['data_entrega'],
            "situacao": self.test_values['situacao'],
            "projeto": self.projeto.id
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_request_nome_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando o nome não é passado"""

        initial_count = Artefato.objects.count()
        request_data = {
            "data_entrega": self.test_values['data_entrega'],
            "situacao": self.test_values['situacao'],
            "projeto": self.projeto.id
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem nome")

    def test_post_request_data_entrega_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando a data de entrega não é passada"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "situacao": self.test_values['situacao'],
            "projeto": self.projeto.id
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem data de entrega")

    def test_post_request_situacao_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando a situação não é passada"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "data_entrega": self.test_values['data_entrega'],
            "projeto": self.projeto.id
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem situação")

class test_artifact_filtering_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.ProjetoTest = Projeto.objects.create(
            nome="Projeto teste", 
            data_inicio='2022-01-01', 
            data_termino='2022-12-31', 
            situacao="Iniciado"
        )

        self.data = {
            "nome": "Artefato teste",
            "descricao": "Artefato teste",
            "data_entrega": "2023-01-01",
            "situacao": "Em andamento",
            "projeto": self.ProjetoTest.id
        }

        self.register_url = reverse_lazy('artifacts:registrar')
        self.list_url = reverse_lazy('artifacts:listar')



    def test_request(self):
        """Verifica se a requisição retornou com status 200"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)

    def test_amount_of_existing_objects(self):
        """Verifica a quantidade de objetos existentes"""
        self.client.post(self.register_url, self.data)
        objetos = Artefato.objects.all()
        self.assertEquals(len(objetos),1)

    def test_filter_by_name(self):
        """Verifica se a filtragem por nome funciona"""
        
        self.client.post(self.register_url, self.data)

        response = self.client.get(reverse_lazy("artifacts:home"), nome='Artefato teste')
        self.assertEquals(response.status_code, 200)
    
    def test_render(self):
        """Veririca se os artefatos foram renderizados na tela"""
        self.client.post(self.register_url, self.data)
        
        response = self.client.get(reverse_lazy("artifacts:home"),{'nome': 'Artefato'})
        self.assertContains(response, ' <td>Artefato teste</td>')
        self.assertTrue('artifacts' in response.context)
      
class DeleteArtifactView(TestCase):

        def setUp(self):
            self.client = Client()
            self.projeto = Projeto.objects.create( nome="Projeto teste", data_inicio='2022-01-01', data_termino='2022-12-31', situacao="Iniciado")
            self.artifact = Artefato.objects.create( nome="Projeto teste",data_entrega='2022-01-01', situacao="Iniciado", projeto =  self.projeto  )
            self.response = self.client.delete(reverse_lazy('artifacts:delete_artifact',  kwargs={'pk': self.artifact.pk}))

        def test_model_content(self):
            self.assertEqual(self.artifact.nome, 'Projeto teste')
            self.assertEqual(self.response.status_code, 302)
            
