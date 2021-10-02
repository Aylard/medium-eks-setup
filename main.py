from flask import Flask, Response

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return Response("<p>Hello, World!</p>")


@ app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return Response("ok")


@ app.route("/connect", methods=['GET'])
def connect():
    return Response("<p>Hello, World!</p>")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
