import unittest
from app import app

class TestPredicaoAPI(unittest.TestCase):
    def setUp(self):
        """
        Método para instanciar app padrao.
        """
        self.client = app.test_client()

    def testar_classe_baixo(self):
        """
        Método para testar a classe 'Lucro baixo'
        """
        tupla = [2014, -0.8660254037844386, 0.5000000000000001, 106, 2049689.4409937887, 7.935949074074074, 7.725, 8.5, 7.725, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        response = self.client.post('/predicao', json={'tupla': tupla})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['resultado'], ['Lucro baixo'])

    def testar_classe_alto(self):
        """
        Método para testar a classe 'Lucro alto'
        """
        dados = [2015,0.49999999999999994,0.8660254037844387,156,93103448.27586207,7.638624338624339,7.85,8.0,7.85,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]
        resp = self.client.post('/predicao', json={'tupla': dados})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()['resultado'], ['Lucro alto'])

    def testar_classe_prejuizo(self):
        """
        Método para testar a classe 'Prejuízo'
        """
        dados = [2022,0.8660254037844386,0.5000000000000001,104,28216245.31914894,6.582870370370371,7.5,6.75,7.5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        resp = self.client.post('/predicao', json={'tupla': dados})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()['resultado'], ['Prejuízo'])

if __name__ == '__main__':
    unittest.main()

