from django.db import models
from django.core.validators import MinLengthValidator
class Estudante(models.Model):
    
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 40)
    cpf = models.CharField(max_length = 11, unique = True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    codigo = models.CharField(validators=[MinLengthValidator(3)], max_length = 10, unique = True)
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 100, choices = NIVEL, blank = False, null = False, default = "B")
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao} ({self.get_nivel_display()})'
    
class Matricula(models.Model):
    
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length = 100, choices = PERIODO, blank = False, null = False, default = 'M')

