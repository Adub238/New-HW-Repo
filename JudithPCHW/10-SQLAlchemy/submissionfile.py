from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

#Python sql toolkit atnd Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

engine=create_engine("sqlite:///Resources/hawaii.sqlite")

Base=automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
#'measurement', 'station' -->save reference to each table
Measurement = Base.classes.measurement
Station=Base.classes.station

session=Session(engine)

#Design a query to retrieve the last 12 months of precipitation data and plot the results
#calculate the date 1 year ago from the last given point in the data base
session.query(Measurement.date).order_by(Measurement.date.desc()).first() #returns latest date
date=dt.datetime(2016, 8, 24) #date year earlier from result
sel=[Measurement.station,
	  Measurement.date,
	  Measurement.prcp]
precipitation=session.query(*sel).filter(Measurement.date>date).order_by(Measurement.date).all()

#Perform a query to retrieve the data and precipitation scores
#results=session.query(Measurement.prcp).filter(Measurement.date>date).all() #making the query


#Save the query results into a pandas df and set the index to the date column
df=pd.DataFrame(precipitation, columns=['station', 'date', 'prcp'])

#sort the dataframe by date
df.set_index('date', inplace=True)
print(df.head())

#Use plotting with Pandas to plot the data
df.plot(rot=90)
plt.show()

# Use Pandas to calculate the summary statistics for the precipitation data
print(df.describe())

# Design a query to show how many stations are available in this dataset?
print(session.query(Station.station).count())

# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.
groupies=session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).all()
groupies_df=pd.DataFrame(groupies, columns=['station', 'count'])
print(groupies_df.sort_values(by='count', ascending=False))

# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?
sele = [Measurement.station, 
       func.min(Measurement.tobs), 
       func.max(Measurement.tobs), 
       func.avg(Measurement.tobs)]
pop_station = session.query(*sele).\
    filter(Measurement.station=='USC00519281').\
    group_by(Measurement.station).\
    order_by(Measurement.station).all()
print(pop_station)

# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
#results=session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.station=='USC00519281')

select = [Measurement.tobs,
        Measurement.date]
temp_station = session.query(*select).\
    filter(Measurement.date > '2016-08-18').\
    filter(Measurement.station=='USC00519281').\
    order_by(Measurement.date).all()
temp_station_df = pd.DataFrame(temp_station,columns=['temp','date'])
temp_station_df.set_index('date', inplace=True)
print(temp_station_df.head(12))

temp_station_df.plot.hist(bins=12)
plt.xlabel('Temperature')
plt.tight_layout()

# This function called `calc_temps` will accept start date and end date in the format%Y-%m-%d' 
def calc_temps(start_date, end_date):
    if start_date >= end_date:
        print(f'Error: {end_date} is earlier than {start_date}. Please enter a valid date.')
    else:
        temp_min=session.query(func.min(Measurement.tobs)).\
            filter(Measurement.station=='USC00519281').\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).all()
        temp_max=session.query(func.max(Measurement.tobs)).\
            filter(Measurement.station=='USC00519281').\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).all()
        temp_avg=session.query(func.avg(Measurement.tobs)).\
            filter(Measurement.station=='USC00519281').\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).all()
        print(f"""The projected lowest temperature for your trip is {temp_min}.
The projected highest temperature for your trip is {temp_max}.
The projected average temperature for your trip is {temp_avg}.""")

calc_temps('2016-02-14', '2016-02-22')



