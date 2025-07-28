from flask import Flask, request, jsonify
from service import ServicoPredicaoFilmes

app = Flask(__name__)
servico = ServicoPredicaoFilmes('modelo/melhor_modelo.pkl')

@app.route('/predicao', methods=['POST'])
def predicao():
    try:
        data = request.get_json()
        tupla = data.get('tupla')
        resultado = servico.previsao(tupla)
        return jsonify({'resultado': [int(elemento) for elemento in resultado]})
    except( TypeError, ValueError) as e:
        print(e)
        return jsonify({'Erro': 'Parametros Inválido'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)