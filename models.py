from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date_of_stay = Column(Date, nullable=False)
    comment = Column(Text, nullable=True)
    rating_proprete = Column(Integer, nullable=True)
    rating_personnel = Column(Integer, nullable=True)
    rating_situation_geographique = Column(Integer, nullable=True)
    rating_chambre = Column(Integer, nullable=True)
    rating_restauration = Column(Integer, nullable=True)
    rating_equipement = Column(Integer, nullable=True)
    rating_wifi = Column(Integer, nullable=True)
    rating_parking = Column(Integer, nullable=True)
    rating_pool = Column(Integer, nullable=True)
    rating_spa = Column(Integer, nullable=True)
    rating_salle_de_sport = Column(Integer, nullable=True)
    rating_transport = Column(Integer, nullable=True)
    rating_navette_aeroport = Column(Integer, nullable=True)
    rating_service_enfant = Column(Integer, nullable=True)
    rating_bar = Column(Integer, nullable=True)
    rating_rapport_qualite_prix = Column(Integer, nullable=True)
