from flask import request, Flask, jsonify
import sqlite3
import os
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

def fun_sumar(num_1, num_2):
    total = num_1 + num_2
    return total

@app.route("/", methods = ["GET"])
def main():
    return "API de libros"


@app.route("/libros", methods = ["GET"])
def libros():
    con = sqlite3.connect("books.db")
    cursor = con.cursor()
    query = "SELECT * FROM books"
    result = cursor.execute(query).fetchall()
    con.close()

    return jsonify(result)

@app.route("/buscar_libros", methods = ["GET"])
def buscar_libros():
    # http://127.0.0.1:5000/buscar_libros?nombre_autor=Paolo
    con = sqlite3.connect("books.db")
    autor = request.args["nombre_autor"]
    cursor = con.cursor()
    query = f"SELECT * FROM books WHERE author LIKE '%{autor}%'"
    result = cursor.execute(query).fetchall()
    con.close()

    return jsonify(result)

@app.route("/buscar_libros_2/<string:autor>", methods = ["GET"])
def buscar_libros_2(autor):
    # http://127.0.0.1:5000/buscar_libros_2/Paolo
    con = sqlite3.connect("books.db")
    cursor = con.cursor()
    query = f"SELECT * FROM books WHERE author LIKE '%{autor}%'"
    result = cursor.execute(query).fetchall()
    con.close()

    return jsonify(result)

@app.route("/buscar_libros_3", methods = ["GET"])
def buscar_libros_3():
    # http://127.0.0.1:5000/buscar_libros_3
    # JSON EJEMPLO:
    """
        {
        "autor":"Ann",
        }
    """
    data = request.get_json()
    autor = data.get("autor")

    con = sqlite3.connect("books.db")
    cursor = con.cursor()
    query = f"SELECT * FROM books WHERE author LIKE '%{autor}%'"
    result = cursor.execute(query).fetchall()
    con.close()

    return jsonify(result)

app.run()

# 1.Ruta para obtener todos los libros