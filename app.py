from flask import Flask, request, jsonify
from service import ServicoPredicaoFilmes

app = Flask(__name__)
servico = ServicoPredicaoFilmes('modelo/melhor_modelo.pkl')

@app.route('/predicao', methods=['POST'])
def predicao():
    """
    Funcao para instanciar o serviço de predição e colocar na aplicação web como json.
    """
    try:
        data = request.get_json()
        tupla = data.get('tupla')
        resultado = servico.previsao(tupla)
        return jsonify({'resultado': resultado.tolist()})
    except( TypeError, ValueError) as e:
        print(e)
        return jsonify({'Erro': 'Parametros Inválido'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)