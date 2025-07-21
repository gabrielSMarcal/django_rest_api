
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Estudante
from escola.serializers import EstudanteSerializer


class EstudantesUserTests(APITestCase):
    
    def setUp(self):
        
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        
        self.estudante = Estudante.objects.create(
            nome='Teste estudante UM',
            email='teste1@example.com',
            cpf='57941363089',
            data_nascimento='2000-01-01',
            celular = '11 99999-9999'
        )
        self.estudante2 = Estudante.objects.create(
            nome='Teste estudante DOIS',
            email='teste2@example.com',
            cpf='28576747081',
            data_nascimento='1995-05-05',
            celular = '11 88888-8888'
        )
        
    def test_requisicao_get_para_listar_estudantes(self):

        """Teste de requisição GET para listar estudantes"""
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):

        """Teste de requisição GET para listar um estudante"""

        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializado = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializado)
        
    def test_requisicao_post_para_criar_um_estutande(self):

        """Teste de requisição POST para criar um estudante"""

        dados = {
            'nome': 'Teste novo',
            'email': 'teste@gmail.com',
            'cpf': '38312389016',
            'data_nascimento': '2000-01-01',
            'celular': '11 99999-9999'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)