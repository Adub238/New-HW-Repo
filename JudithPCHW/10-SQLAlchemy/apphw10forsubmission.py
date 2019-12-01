import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Database Setup
engine=create_engine('sqlite:///Resources/hawaii.sqlite')

Base=automap_base()

Base.prepare(engine, reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station

app=Flask(__name__)

@app.route('/')
def welcome():
    #List all available api routes
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )
        
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of measurement values with date as the key, prcp as the value"""
    # Query all dates
    results = session.query(Measurement.date, Measurement.prcp).\
        group_by(func.strftime("%Y-%m-%d", Measurement.date)).all()
    session.close()

    # Create a dictionary from the measurement data and append to a list of all_precipitation
    all_precipitation = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_precipitation.append(measurement_dict)

    return jsonify(all_precipitation)
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results=session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results2=session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        group_by(func.strftime("%Y-%m-%d", Measurement.date)).all()
    session.close()
    # Create a dictionary from the measurement data and append to a list of all_precipitation
    annual_temperature_results=[]
    for date, tobs in results2:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["tobs"] = tobs
        annual_temperature_results.append(temperature_dict)

    return jsonify(annual_temperature_results)
    
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_avg(start=None, end=None):
    select = [func.min(Measurement.tobs), 
       func.max(Measurement.tobs), 
       func.avg(Measurement.tobs)]
    if not end:
        session=Session(engine)
        results=session.query(*select).filter(Measurement.station=='USC00519281').\
            filter(Measurement.date > start).\
            group_by(func.strftime("%Y-%m-%d",Measurement.date)).all()
        session.close()
        return jsonify(results)
    session=Session(engine)
    capped_results=session.query(*select).\
        filter(Measurement.date> start).\
        filter(Measurement.date< end).\
        group_by(func.strftime("%Y-%m-%d",Measurement.date)).all()
    session.close()
    return jsonify(capped_results)

if __name__ == '__main__':
    app.run(debug=True)
