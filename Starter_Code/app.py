# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> (type start date )<br/>"
        f"/api/v1.0/<start>/<end> (type start/end date )<br/>"
        f"For dates, please use YYYY-MM-DD format"
)

@app.route("/api/v1.0/precipitation")
def precipitation():
    "Return query results from precipitation analysis."

    #Query precipitation data from the last 12 months of data
    most_recent_date = dt.date(2017,8,23)
    # Calculate the date one year from the last date in data set.
    year_ago = most_recent_date - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    query = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= year_ago).\
        order_by(measurement.date)
    results = query

    session.close()
    
    #Create a dictionary
    prcp_dict = {}
    for date, prcp in results:
        prcp_dict[date] = prcp
        

    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    "Return a JSON list of stations from the dataset"
    results = session.query(station.station, station.name).all()

    session.close()

    #Create a list
    station_list = []
    for result in results:
        station_dict = {"station": result.station,
                        "name": result.name
                       }
        station_list.append(station_dict)

    return jsonify(station_list)
    

@app.route("/api/v1.0/tobs")
def tobs():
    "Return a JSON list of temperature observations"

     #Query precipitation data from the last 12 months of data
    most_recent_date = dt.date(2017,8,23)
    # Calculate the date one year from the last date in data set.
    year_ago = most_recent_date - dt.timedelta(days=365)

    results = session.query(measurement.date,measurement.tobs).\
            filter(measurement.date >= year_ago, measurement.station == 'USC00519281').\
            order_by(measurement.date)


    session.close()

    tobs_list = []
    for date, tobs in results:
        tobs_dict = {"date": date,
                     "tobs": tobs
                    }
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)
    


@app.route("/api/v1.0/<start>")
def start(start):

    try:
        start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400

    results = session.query(func.min(measurement.tobs), 
                            func.max(measurement.tobs),func.avg((measurement.tobs)).\
                            filter(measurement.date >= start_date)).all()

    session.close()
    min_temp, max_temp, avg_temp = results[0]

    temp_stats = {
        "Start Date": start,
        "Min Temperature": min_temp,
        "Max Temperature": max_temp,
        "Average Temperature": avg_temp
    }
    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    try:
        start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
        end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400

    results = session.query(func.min(measurement.tobs), 
                            func.max(measurement.tobs),func.avg((measurement.tobs)).\
                            filter(measurement.date >= start_date,
                                   measurement.date <= end_date)).all()

    session.close()
    min_temp, max_temp, avg_temp = results[0]

    temp_stats = {
        "Start Date": start,
        "End Date": end,
        "Min Temperature": min_temp,
        "Max Temperature": max_temp,
        "Average Temperature": avg_temp
    }
    return jsonify(temp_stats)


if __name__ == '__main__':
    app.run(debug=True)










