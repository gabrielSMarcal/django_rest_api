
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
        
        self.estudante = Estudante.objects.create(
            nome = 'Estudante Teste',
            email = 'teste@example.com',
            cpf = '42070997006',
            data_nascimento = '2000-01-01',
            celular = '11 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo = 'CURSO001',
            descricao = 'Curso de Teste UM',
            nivel = 'B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo = 'M'
        )
        
    def test_requisicao_get_para_listar_matriculas(self):
        
        """Teste de requisição GET para listar matrículas"""
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)