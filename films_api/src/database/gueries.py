"""
SELECT QUERIES
"""
from src.app import db
from src.database import models

films = db.session.query(models.Film).order_by(models.Film.rating).all()
print(films)