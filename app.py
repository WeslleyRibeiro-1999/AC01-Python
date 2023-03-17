from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def nota():
    nota1 = request.args.get('n1')
    nota2 = request.args.get('n2')

    media = (int(nota1) + int(nota2)) / 2

    response = f'Sua media foi {media}'

    return  response


if __name__ == '__main__':
    app.run(debug=True, port=8080)