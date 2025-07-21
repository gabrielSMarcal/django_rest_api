
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Estudante, Matricula, Curso

class MatriculasUserTests(APITestCase):
    
    def setUp(self):
        
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        
        self.estudante1 = Estudante.objects.create(
            nome = 'Estudante Teste',
            email = 'teste@example.com',
            cpf = '42070997006',
            data_nascimento = '2000-01-01',
            celular = '11 99999-9999'
        )
        self.estudante2 = Estudante.objects.create(
            nome = 'Estudante Teste 2',
            email = 'teste2@example.com',
            cpf = '53345749050',
            data_nascimento = '2000-01-02',
            celular = '11 99999-9998'
        )
        self.curso1 = Curso.objects.create(
            codigo = 'CURSO001',
            descricao = 'Curso de Teste UM',
            nivel = 'B'
        )
        self.curso2 = Curso.objects.create(
            codigo = 'CURSO002',
            descricao = 'Curso de Teste DOIS',
            nivel = 'I'
        )
        self.matricula1 = Matricula.objects.create(
            estudante=self.estudante1,
            curso=self.curso1,
            periodo = 'M'
        )
        self.matricula2 = Matricula.objects.create(
            estudante=self.estudante2,
            curso=self.curso2,
            periodo = 'V'
        )
        
    def test_requisicao_get_para_listar_matriculas(self):
        
        """Teste de requisição GET para listar matrículas"""
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)