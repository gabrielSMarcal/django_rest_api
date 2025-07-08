from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudante, ListaMatriculasCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='Estudantes')
router.register(r'cursos', CursoViewSet, basename='Cursos')
router.register(r'matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view())
]
