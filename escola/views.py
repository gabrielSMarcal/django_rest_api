from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from escola.throttles import MatriculaAnonRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de Estudantes.

    Funcionalidades:
    - Permite criar, listar, recuperar, atualizar e deletar estudantes (CRUD).
    - Suporta busca e ordenação pelos campos 'nome' e 'cpf'.
    - Seleciona automaticamente o serializer conforme a versão da API requisitada.

    Parâmetros de busca e ordenação:
    - nome (str): Nome do estudante.
    - cpf (str): CPF do estudante.

    Versão da API:
    - v1: Utiliza EstudanteSerializer.
    - v2: Utiliza EstudanteSerializerV2.

    Métodos permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Observações:
    - Utiliza filtros do DjangoFilterBackend, OrderingFilter e SearchFilter.
    """
    queryset = Estudante.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de Cursos.

    Funcionalidades:
    - Permite criar, listar, recuperar, atualizar e deletar cursos (CRUD).

    Parâmetros:
    - id (int): Identificador primário do curso.

    Métodos permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Observações:
    - Os cursos são ordenados pelo campo 'id'.
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de Matrículas.

    Funcionalidades:
    - Permite listar todas as matrículas e criar novas matrículas.

    Parâmetros:
    - id (int): Identificador primário da matrícula.

    Métodos permitidos:
    - GET: Lista todas as matrículas.
    - POST: Cria uma nova matrícula.

    Observações:
    - Não permite atualização ou exclusão de matrículas via API.
    - Aplica limitação de requisições por usuário autenticado e anônimo (throttling).
    - Matrículas são ordenadas pelo campo 'id'.
    """
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ['get', 'post']
    
class ListaMatriculasEstudante(generics.ListAPIView):
    
    '''
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''
    
    def get_queryset(self):
        
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculasCurso(generics.ListAPIView):
    
    '''
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''

    def get_queryset(self):
        
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer