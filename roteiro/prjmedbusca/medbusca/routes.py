from medbusca import app
from .models import Setor
from flask import Flask,render_template

@app.route('/')
def cliente():
    with app.app_context():
         setor = Setor.query.all()
    return render_template('cliente.html',setor = setor)

