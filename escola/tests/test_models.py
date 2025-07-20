from django.test import TestCase

from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    
    def test_falha(self):
        message = 'Faiou =('
        self.fail(message)