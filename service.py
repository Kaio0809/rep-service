import joblib
import pandas as pd

class ServicoPredicaoFilmes:
    def __init__(self, modelo):
        self.model = joblib.load(modelo)

    def previsao(self, tupla_releases):
        X_ft = ['ano_lancamento', 'mes_seno', 'mes_cos', 'duracao', 'orcamento',
            'media_elenco', 'media_direcao', 'mediana_elenco', 'mediana_direcao',
            'Drama', 'Mystery', 'Action', 'Family', 'Documentary', 'Crime', 'Romance',
            'War', 'Comedy', 'Fantasy', 'Adventure', 'Thriller', 'Science Fiction',
            'Western', 'History', 'Horror', 'Animation', 'Music', 'TV Movie',
            'categoria_lucro']
        
        dataset = pd.DataFrame([tupla_releases], columns=X_ft)
        X = dataset[X_ft]
        return self.model.predict(X)