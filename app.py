from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World, this is Rafael Barros"

if __name__ == '__main__':
    app.run()