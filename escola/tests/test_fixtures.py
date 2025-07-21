from django.test import TestCase

from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']
    
    def test_estudante_fixtures(self):
        
        """Testa se os estudantes foram carregados corretamente."""
        
        estudante = Estudante.objects.get(cpf='65854858401')
        curso = Curso.objects.get(pk=4)
        self.assertEqual(estudante.celular, '56 94260-6383')
        self.assertEqual(curso.codigo, 'CDJ01')