from django.test import TestCase

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    
    def setUp(self):
        
        self.estudante = Estudante(
            nome='Teste de Serializer',
            email='teste@serializer.com',
            cpf='71427904073',
            data_nascimento='2000-01-01',
            celular='11 98765-4321'
        )
        
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)
        
    def test_serializer_estudante(self):
        
        """Confirma os dados serializados do estudante"""
        
        dados = self.serializer_estudante.data
        
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))
        
    def test_conteudo_dos_campos_serializados(self):
        
        """Confirma o conteúdo dos campos serializados do estudante"""
        
        dados = self.serializer_estudante.data
        
        dados = self.serializer_estudante.data
        
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['celular'], self.estudante.celular)
        
class SerializerCursoTestCase(TestCase):
    
    def setUp(self):
        
        self.curso = Curso(
            codigo='CUR456',
            descricao='Curso de Serializer',
            nivel='B'
        )
        
        self.serializer_curso = CursoSerializer(instance=self.curso)
        
    def test_serializer_curso(self):
        
        """Confirma os dados serializados do curso"""
        
        dados = self.serializer_curso.data
        
        self.assertEqual(set(dados.keys()), set(['id', 'codigo', 'descricao', 'nivel']))
        
    def test_conteudo_dos_campos_serializados_curso(self):
        
        """Confirma o conteúdo dos campos serializados do curso"""
        
        dados = self.serializer_curso.data
        
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)
        
class SerializerMatriculaTestCase(TestCase):
    
    def setUp(self):
        
        self.estudante_matricula = Estudante.objects.create(
            nome='Estudante Teste',
            email='estudante@teste.com',
            cpf='71427904073',
            data_nascimento='2000-01-01',
            celular='11 98765-4321'
        )

        self.curso_matricula = Curso.objects.create(
            codigo='CUR456',
            descricao='Curso de Teste',
            nivel='B'
        )

        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )

        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_serializer_matricula(self):

        """Confirma os dados serializados da matrícula"""

        dados = self.serializer_matricula.data

        self.assertEqual(set(dados.keys()), set(['id','periodo', 'estudante', 'curso']))

    def test_conteudo_dos_campos_serializados_matricula(self):

        """Confirma o conteúdo dos campos serializados da matrícula"""

        dados = self.serializer_matricula.data

        self.assertEqual(dados['estudante'], self.estudante_matricula.id)
        self.assertEqual(dados['curso'], self.curso_matricula.id)
        self.assertEqual(dados['periodo'], self.matricula.periodo)
