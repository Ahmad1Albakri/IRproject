from flask import Flask, request

app = Flask(__name__)


@app.route('/search',methods=["POST"])
def hello_world():
    query = request.form.get('query')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
