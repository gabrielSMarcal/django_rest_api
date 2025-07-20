from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserTests(APITestCase):
    
    def setUp(self):
        
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Estudantes-list')
        
    def test_autenticacao_com_credenciais_validas(self):
        
        """Testa a autenticação com credenciais válidas."""
        
        usuario = authenticate(
            username='admin',
            password='admin'
        )
        
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
        
    def test_autenticacao_com_usuario_incorreto(self):

        """Testa a autenticação com usuário incorreto."""
        
        usuario = authenticate(
            username='amin',
            password='admin'
        )
        
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
    def test_autenticacao_com_senha_incorreta(self):
        
        """Testa a autenticação com senha incorreta."""
        
        usuario = authenticate(
            username='admin',
            password='amin'
        )
        
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
    def test_requisicao_get_autorizada(self):
        
        """Testa a requisição GET autorizada."""

        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_get_nao_autorizada(self):
        
        """Testa a requisição GET não autorizada."""
        
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
