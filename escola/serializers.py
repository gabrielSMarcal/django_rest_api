from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
        
    def validate(self, dados):
        
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve ter exatamente 11 dígitos.'})
    
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})
        
        if len(dados['celular']) != 13:
            raise serializers.ValidationError({'celular':'O celular deve ter exatamente 13 caracteres.'})
        
        return dados
    

    
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Curso
        fields = '__all__'
    
class MatriculaSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Matricula
        exclude = []
    
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        
        model = Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        
        model = Matricula
        fields = ['estudante_nome']
        