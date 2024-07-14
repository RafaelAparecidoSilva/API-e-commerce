from app import app, db


# Criando as tabelas no banco de dados
with app.app_context():
    db.create_all()
    db.session.commit()
