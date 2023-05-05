"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="postgres://root:IzN1uQ4hyQLyTeeXkQzLXt68ZoGd6lUb@dpg-chaafeqk728r886f0u20-a.oregon-postgres.render.com",
        database="todo_kz9p",
        user="root",
        password="IzN1uQ4hyQLyTeeXkQzLXt68ZoGd6lUb")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
