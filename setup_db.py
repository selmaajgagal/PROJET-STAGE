from sqlalchemy import create_engine
from models import Base


engine = create_engine('sqlite:///feedback.db')  
Base.metadata.create_all(engine)  

print("Database and tables created successfully.")
