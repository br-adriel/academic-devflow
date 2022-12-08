from ast import Return
from django.test import TestCase,Client
from django.urls import reverse_lazy,reverse
from projects.models import Projeto
from projects.views import update_view,project_list

class TestViewNewProject(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse_lazy('projects:registrar')
        self.ProjectTest = Projeto.objects.create(
            nome = 'Nome teste',
            descricao = 'Descrição teste',
            data_inicio = '2010-10-10',
            data_termino = '2011-11-11',
            situacao = 'Em desenvolvimento'
        )

    def test_view_new_project(self):
        url = self.register_url
        data = {
            "nome": self.ProjectTest.nome,
            "descricao": self.ProjectTest.descricao,
            "data_inicio": self.ProjectTest.data_inicio,
            "data_termino": self.ProjectTest.data_termino,
            "situacao": self.ProjectTest.situacao
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.ProjectTest.nome, 'Nome teste')



class ProjetoUpdateView(TestCase):
    DESCRICAO = 'Teste do modelo projeto'
    DT_INICIO = '2010-10-10'
    DT_TERMINO = '2011-11-11'
    NOME = 'Teste'
    SITUACAO = 'Em desenvolvimento'

    def setUp(self):
        self.PROJETO_OBJ = Projeto.objects.create(
            descricao=self.DESCRICAO, 
            data_inicio=self.DT_INICIO,
            data_termino=self.DT_TERMINO, 
            nome=self.NOME, 
            situacao=self.SITUACAO)

        self.update_url = reverse_lazy('projects:atualizar', kwargs={'pk': self.PROJETO_OBJ.pk})

                    

    def test_nome_do_projeto_editavel(self):
        """Testa se o campo 'nome' de um objeto Projeto é editável"""

        novo_nome = "nome 2"
        data = {
            "descricao": self.PROJETO_OBJ.descricao,
            "data_inicio": self.PROJETO_OBJ.data_inicio,
            "data_termino": self.PROJETO_OBJ.data_termino,
            "nome": novo_nome,
            "situacao": self.PROJETO_OBJ.situacao
        }
        self.client.post(self.update_url, data)

        projeto_atualizado = Projeto.objects.filter(nome=novo_nome).first()
        self.assertIsNotNone(projeto_atualizado)

class ProjetoGetAllProjets(TestCase):

    DESCRICAO = 'Teste do modelo projeto'
    DT_INICIO = '2010-10-10'
    DT_TERMINO = '2011-11-11'
    NOME = 'Teste'
    SITUACAO = 'Em desenvolvimento'

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('projects:listar')
        self.objeto = Projeto.objects.create(descricao=self.DESCRICAO, data_inicio=self.DT_INICIO,
                                                  data_termino=self.DT_TERMINO, nome=self.NOME, situacao=self.SITUACAO)

    def test_project_list(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response, 'projects/index.html')

        
    def test_get_some(self): 
        
        response = self.client.get(self.list_url)
        objetos  = Projeto.objects.all()
        
        self.assertEquals(response.status_code,200)
        # self.assertTrue(objetos)

class TestViewDeleteProject(TestCase):

    def setUp(self):
        self.client = Client()
        self.ProjectTest = Projeto.objects.create(
            nome = 'Nome teste',
            descricao = 'Descrição teste',
            data_inicio = '2010-10-10',
            data_termino = '2011-11-11',
            situacao = 'Em desenvolvimento'
        )

        self.register_url = reverse_lazy('projects:excluir', kwargs={'pk': self.ProjectTest.pk})

    def test_view_delete_project(self):
        url = self.register_url

        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)



