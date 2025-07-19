from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from escola.throttles import MatriculaAnonRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
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
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ['get', 'post']
    
class ListaMatriculaEstudante(generics.ListAPIView):
    """
    API View para listar todas as matrículas de um estudante específico.

    Funcionalidades:
    - Retorna todas as matrículas associadas ao estudante identificado pelo parâmetro 'pk'.

    Parâmetros de URL:
    - pk (int): Identificador primário do estudante cujas matrículas serão listadas.

    Métodos permitidos:
    - GET

    Observações:
    - O resultado é ordenado pelo campo 'id' da matrícula.
    - Retorna uma lista detalhada das matrículas do estudante, incluindo informações do curso e do período.
    """
    serializer_class = ListaMatriculasEstudanteSerializer

    def get_queryset(self):
        # Evita erro durante a geração do schema
        if getattr(self, 'swagger_fake_view', False):
            return Matricula.objects.none()
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')

class ListaMatriculaCurso(generics.ListAPIView):
    """
    API View para listar todas as matrículas de um curso específico.

    Funcionalidades:
    - Retorna todas as matrículas associadas ao curso identificado pelo parâmetro 'pk'.

    Parâmetros de URL:
    - pk (int): Identificador primário do curso cujas matrículas serão listadas.

    Métodos permitidos:
    - GET

    Observações:
    - O resultado é ordenado pelo campo 'id' da matrícula.
    - Retorna uma lista detalhada dos estudantes matriculados no curso, incluindo informações do estudante e do período.
    """
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        # Evita erro durante a geração do schema
        if getattr(self, 'swagger_fake_view', False):
            return Matricula.objects.none()
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')