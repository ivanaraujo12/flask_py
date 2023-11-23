from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder= 'templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://nb.db'
database = SQLAlchemy(app)

class Usuario(database.Model):
    id_setor = database.Column(database.Integer,primary_key=True)
    nome_setor = database.Column(database.String, nullable=False, unique=True)

@app.route('/')

def cliente():
   usuario = Usuario.query.all()
   return render_template("cliente.html", usuario = usuario )




if __name__ == '__main__':
    app.run(debug=True)
