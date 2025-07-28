import joblib
import pandas as pd

class ServicoPredicaoFilmes:
    def __init__(self, modelo):
        self.model = joblib.load(modelo)

    def previsao(self, tupla_releases):
        """
        Método que usa o modelo usado para prever a classe do filme.
        tupla_releases: lista com features para a previsao

        return : resultado da previsão de acordo com o modelo passado.
        """
        
        X_ft = ['ano_lancamento', 'mes_seno', 'mes_cos', 'duracao', 'orcamento',
            'media_elenco', 'media_direcao', 'mediana_elenco', 'mediana_direcao',
            'Drama', 'Mystery', 'Action', 'Family', 'Documentary', 'Crime', 'Romance',
            'War', 'Comedy', 'Fantasy', 'Adventure', 'Thriller', 'Science Fiction',
            'Western', 'History', 'Horror', 'Animation', 'Music', 'TV Movie']
        
        dataset = pd.DataFrame([tupla_releases], columns=X_ft)
        X = dataset[X_ft]
        return self.model.predict(X)