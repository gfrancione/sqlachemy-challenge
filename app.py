# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# Create an SQLite engine
# Define the path to your SQLite database file
database_path = "C:/Users/gfran/Desktop/ASU-VIRT-DATA-PT-03-2023-U-LOLC-1/Homework/Module-10/Starter_Code/Resources/hawaii.sqlite"

# Create the SQLAlchemy engine
engine = create_engine(f"sqlite:///{database_path}")

#Confirm operation
from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()

if "measurement" in tables and "station" in tables:
    print("Tables 'measurement' and 'station' exist in the database.")
else:
    print("One or both of the tables is missing in the database.")


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Save references to each table
from sqlalchemy.orm import Session

# Create a session
session = Session(engine)

# Query data from the measurement table
results = session.query(Measurement).all()


# Create our session (link) from Python to the DB
# Define the path to your SQLite database file

# Create the SQLAlchemy engine

# Define the path to your SQLite database file
database_path = "C:/Users/gfran/Desktop/ASU-VIRT-DATA-PT-03-2023-U-LOLC-1/Homework/Module-10/Starter_Code/Resources/hawaii.sqlite"

# Create the SQLAlchemy engine
engine = create_engine(f"sqlite:///{database_path}")


#################################################
# Flask Setup
#################################################
from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')





#################################################
# Flask Routes
#################################################
