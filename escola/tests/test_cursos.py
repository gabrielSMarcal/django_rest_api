
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Curso


class CursosUserTests(APITestCase):
    
    def setUp(self):
        
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        
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
        
    def test_requisicao_get_para_listar_cursos(self):
        
        """Teste de requisição GET para listar cursos"""
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
