# this is the "web_app/__init__.py" file...

from flask import Flask
import os

from web_app.routes.home_routes import home_routes
from web_app.routes.stock_routes import stocks_routes
from web_app.routes.unemployment_routes import unemployment_routes
from web_app.routes.product_routes import product_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(stocks_routes)
    app.register_blueprint(unemployment_routes)
    app.register_blueprint(product_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)