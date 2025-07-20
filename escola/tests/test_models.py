from django.test import TestCase

from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    
    # def test_falha(self):
    #     message = 'Faiou =('
    #     self.fail(message)
    
    def setUp(self):
        
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@modelo.com',
            cpf = '71427904073',
            data_nascimento = '2000-01-01',
            celular = '11 98765-4321'
        )
    
    def test_verificacao_de_estudante(self):
        
        """Confirma os atributos do estudante"""
        
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'teste@modelo.com')
        self.assertEqual(self.estudante.cpf, '71427904073')
        self.assertEqual(self.estudante.data_nascimento, '2000-01-01')
        self.assertEqual(self.estudante.celular, '11 98765-4321')
        
class ModelCursoTestCase(TestCase):
    
    def setUp(self):
        
        self.curso = Curso.objects.create(
            codigo = 'CUR123',
            descricao = 'Curso de Teste',
            nivel = 'B'
        )
        
    def test_verificacao_de_curso(self):
        
        """Confirma os atributos do curso"""
        
        self.assertEqual(self.curso.codigo, 'CUR123')
        self.assertEqual(self.curso.descricao, 'Curso de Teste')
        self.assertEqual(self.curso.nivel, 'B')
        
class ModelMatriculaTestCase(TestCase):

    def setUp(self):
        
        self.estudante = Estudante.objects.create(
            nome='Estudante Teste',
            email='estudante@teste.com',
            cpf='71427904073',
            data_nascimento='2000-01-01',
            celular='11 98765-4321'
        )
        
        self.curso = Curso.objects.create(
            codigo='CUR456',
            descricao='Curso de Teste 2',
            nivel='I'
        )
        
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='M'
        )
        
    def test_verificacao_de_matricula(self):
        
        """Confirma os atributos da matrícula"""
        
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'M')