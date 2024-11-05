# sqlalchemy-challenge
Module 10

## Project Overview
The purpose of this project was to utilize SQL Alchemy to conduct a climate analysis of Honolulu, Hawaii. The project begins first with conducting an exploratory analysis of the precipitation and temperature measurments that have occured within the last year. The results of said analysis were then plotted inside a jupyter notebook file in order to visualize the trend in these climate attributes over time. Afterwards a python application utilizing flask was created in order to access the results of the precipitation/station/temperature analysis, while also allowing for an interactive component that would query the temperature data from specified timeframes given by the user.

### Exploratory Analysis:
The jupyter notebook used for the exploratory analysis of this project was titled ["climate_starter"](https://github.com/EdGonz44/sqlalchemy-challenge/blob/main/Starter_Code/climate_starter.ipynb), and made queries  [sqllite file](https://github.com/EdGonz44/sqlalchemy-challenge/blob/main/Starter_Code/Resources/hawaii.sqlite) of the combined csv files for the stations in Hawaii ["Stations"](https://github.com/EdGonz44/sqlalchemy-challenge/blob/main/Starter_Code/Resources/hawaii_stations.csv), and the climate data taken from said stations over time ["Measurements"](https://github.com/EdGonz44/sqlalchemy-challenge/blob/main/Starter_Code/Resources/hawaii_measurements.csv). 

## App.py:
The python [application](https://github.com/EdGonz44/sqlalchemy-challenge/blob/main/Starter_Code/app.py) created utilizes flask as a means of displaying the results found from the exploratory analysis notebook, while also providing two interactive routes to access temperature data based on user input.



## Project Structure
The project repository should have the following structure:

```plaintext
sqlalchemy-challenge/
│
├── Starter_Code
|   ├── Resources
|       ├── hawaii.sqllite
|       ├──hawaii_measurements.csv
|       ├──hawaii_stations.csv
|  ├──app.py
|  ├──climate_starter.ipynb
└──README.md

```
