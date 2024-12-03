from flask import Blueprint, render_template
import requests
import os

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products")
def products_list():
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(url)
    
    if response.status_code == 200:
        drinks = response.json().get("drinks", [])
    else:
        drinks = []
    
    return render_template("products.html", products=drinks)