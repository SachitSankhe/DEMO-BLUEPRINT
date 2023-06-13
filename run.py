from apiflask import APIFlask
from flask import jsonify
from app import bp

app = APIFlask(__name__)


app.register_blueprint(bp,url_prefix="/blueprint")


if __name__ == "__main__":

    app.run(debug=True)
