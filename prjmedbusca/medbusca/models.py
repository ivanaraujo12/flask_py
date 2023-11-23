from medbusca import database

class Setor(database.Model):
    id_setor = database.Column(database.Integer, primary_key=True)
    nome_setor = database.Column(database.String, nullable=False, unique=True)