# app.py
# provides the Flask application

from flask import Flask, Response
from sqlalchemy import create_engine

app = Flask(__name__)  # create a Flask app

db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")


@app.route("/", methods=["GET"])
def root() -> Response:
    """
    root - returns 200 OK

    """
    return Response("It's alive!", status=200)


@app.route("/product/<product_id>")
def average_review(product_id: str) -> Response:
    """
    average_review

    TO-DO: ADD DOCUMENTATION
    
    """
    result = db_engine.execute("SELECT * FROM reviews LIMIT 1;").fetchone()

    return Response(str(result), 200)
