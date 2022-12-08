from django.test import TestCase
from artifacts.models import Artefato
from projects.models import Projeto


class ArtefatoModel(TestCase):
    def setUp(self):
        self.DESCRICAO = "Modelo de dados conceitual"
        self.NOME = "Modelo de dados"
        self.SITUACAO = "Entregue"
        self.DATA_ENTREGA = '2022-12-12'
        self.PROJETO = Projeto.objects.create(
            nome="Projeto teste", data_inicio='2022-01-01', data_termino='2022-12-31', situacao="Iniciado")

    def test_objeto_criado_todos_campos(self):
        """O modelo cria corretamente o objeto quando todos os atributos são fornecidos"""

        a = Artefato.objects.create(descricao=self.DESCRICAO, nome=self.NOME,
                                    situacao=self.SITUACAO, data_entrega=self.DATA_ENTREGA,
                                    projeto=self.PROJETO)
        self.assertTrue(isinstance(a, Artefato))
        self.assertEqual(a.nome, self.NOME)

    def test_objeto_criado_campos_obrigatorios(self):
        """O modelo cria corretamente o objeto quando apenas os atributos obrigatórios são fornecidos"""

        a = Artefato.objects.create(nome=self.NOME, situacao=self.SITUACAO,
                                    data_entrega=self.DATA_ENTREGA, projeto=self.PROJETO)
        self.assertTrue(isinstance(a, Artefato))
        self.assertEqual(a.nome, self.NOME)
