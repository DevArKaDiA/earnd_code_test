from flask import Flask
from routes.document import document_blueprint

server = Flask(__name__)
server.debug = True
server.register_blueprint(document_blueprint, url_prefix="/document")

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=8080)