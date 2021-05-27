# app.py
# provides the Flask application

from flask import Flask, Response
from flask import request
from flask import jsonify
from requests.api import request 
from sqlalchemy import create_engine
import requests

app = Flask(__name__)
db_engine= create_engine("sqlite:///data/musical_instrument_reviews.sqlite")

# First route of the API, checks to see if the service is available
@app.route("/", methods=["GET"])
def root():
    """
    root - returns 200 OK
    """
    return Response("It's alive!", status=200)


# Second and third routes return information about a specific product via its productID number
@app.route('/v1/product/<product_id>', methods=['GET'])

# Calculates the average review score from all overall star scores for a specific product via its ID 
def average_reviews(product_id: str):
    average_score = []
    query = 'SELECT ROUND(AVG(overall)) FROM reviews WHERE productID = :productID;'
    result = db_engine.execute(query, productID=product_id).fetchall()
    
    for row in result:
        average_score.append(dict(row))
        
    return jsonify(average_score)


@app.route('/v1/product/review_percentage/<product_id>', methods=['GET'])

# Calculates the percentage of reviews with N stars (e.g. 20% of all reviews are 5 stars) for a specific product via its ID
def percentage_of_reviews(product_id: str):
    reviews_list = []
    
    query = 'SELECT overall,count(overall)*100/sum(count(*))over() FROM reviews WHERE productID =:productID GROUP BY overall;'
    result = db_engine.execute(query, productID=product_id).fetchall()
    
    for row in result:
        reviews_list.append(dict(row))
    return jsonify(reviews_list)


# Fourth route retrives review information from specific users via their ID 
@app.route('/v1/user/<user_id>', methods=['GET'])

# Calculates the average number of stars a particular user gives in their reviews (e.g. on average, this user gives a score of 3 stars)
def average_user_review(reviewer_id: str): 
    average_user_score = []
    query = 'SELECT ROUND(AVG(overall)) FROM reviews WHERE reviewerID = :reviewerID;'
    result = db_engine.execute(query, rewieverID=reviewer_id).fetchall()
    
    for row in result:
        average_user_score.append(dict(row))
        
    return jsonify(average_user_score)

@app.route('/v1/user/user_reviews/<reviewer_id>', methods =['GET'])

# Calculates the percentage of review scores that a user gives in their reviews in total (e.g. 10% of this user's reviews are 3 stars)
def percentage_of_user_reviews(reviewer_id: str):
    user_reviews_list = []
    
    query = 'SELECT overall,count(overall)*100/sum(count(*))over() FROM reviews WHERE reviewerID =:reviewerID GROUP BY overall;'
    result = db_engine.execute(query, reviewerID=reviewer_id).fetchall()
    
    for row in result:
        user_reviews_list.append(dict(row))
    return jsonify(user_reviews_list)


if __name__ == "__main__":
    app.run(debug=True)