
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Estudante, Matricula, Curso

class MatriculasUserTests(APITestCase):
    
    fixtures = ['prototipo_banco.json']
    
    def setUp(self):
        
        self.usuario = User.objects.get(pk=1)
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        
        self.estudante1 = Estudante.objects.get(pk=1)
        self.estudante2 = Estudante.objects.get(pk=2)
        self.curso1 = Curso.objects.get(pk=1)
        self.curso2 = Curso.objects.get(pk=2)
        self.matricula1 = Matricula.objects.get(pk=1) # Precisa criar a matrícula com os dados ligados ao Estudante e Curso 1
        self.matricula2 = Matricula.objects.get(pk=2) # Precisa criar a matrícula com os dados ligados ao Estudante e Curso 1
        
    def test_requisicao_get_para_listar_matriculas(self):
        
        """Teste de requisição GET para listar matrículas"""
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_post_para_criar_uma_matricula(self):
        
        """Teste de requisição POST para criar uma matrícula"""
        
        dados = {
            'estudante': self.estudante1.pk,
            'curso': self.curso1.pk,
            'periodo': 'M'
        }
        
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_para_deletar_uma_matricula(self):
        
        """Teste de requisição DELETE para deletar uma matrícula"""
        
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_requisicao_put_para_atualizar_uma_matricula(self):
        
        """Teste de requisição PUT para atualizar uma matrícula"""
        
        dados = {
            'estudante': self.estudante2.pk,
            'curso': self.curso2.pk,
            'periodo': 'V'
        }
        response = self.client.put(f'{self.url}2/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)