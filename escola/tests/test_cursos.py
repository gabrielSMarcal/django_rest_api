
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Curso
from escola.serializers import CursoSerializer


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
        
    def test_requisicao_get_para_listar_um_curso(self):
        
        """Teste de requisição GET para listar um curso"""
        
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializado = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializado)
        
    
    def test_requisicao_post_para_criar_um_curso(self):
        
        """Teste de requisição POST para criar um curso"""
        
        dados = {
            'codigo': 'CURSO003',
            'descricao': 'Curso de Teste TRÊS',
            'nivel': 'A'
        }
        
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_delete_para_deletar_um_curso(self):
        
        """Teste de requisição DELETE para deletar um curso"""
        
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_requisicao_put_para_atualizar_um_curso(self):
        
        """Teste de requisição PUT para atualizar um curso"""
        
        dados = {
            'codigo': 'CURSO001',
            'descricao': 'Curso de Teste UM Atualizado',
            'nivel': 'B'
        }
        
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)