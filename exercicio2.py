from datetime import date
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='exercicio2',
                         version='1.0')
spec.register(app)
@app.route('/')
def index():
    return jsonify({"hello": "world"})

@app.route('/<quantidade>/<tipo>')
def data_de_validade(quantidade, tipo):
    # Informar a data de validade
    '''
        API para mostras a data de validade dos produtos

        ## Endpoint:
        `GET /<quantidade>/<tipo>`

        ## Parâmetros:
        - `quantidade`: indefinido
        - `tipo`: tipo, mes ano ou dia

        ##Resposta (Json):
        json

        ## Erros Possíveis:
        - se não estiver no formato correto aparecera a msg


    '''

    try:
        data_atual = date.today()
        qtde = int(quantidade)
        if tipo in ["dia", "dias", "day","days"]:
            data_atual + relativedelta(days=qtde)

        return jsonify({"A data de validade do produto é ": data_atual})
    except ValueError:
        return jsonify({'Error': 'Utilize numeros'})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
