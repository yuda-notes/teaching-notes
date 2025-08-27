# Exercise Python & SQL

## Setup
- Install `psycopg2` package
  ```shell
  pip install psycopg2-binary
  ```
- Create table
  ```sql
  DROP TABLE IF EXISTS bikeshare_trips;
  
  CREATE TABLE IF NOT EXISTS bikeshare_trips
  (
      trip_id varchar,
      subscriber_type varchar,
      bike_id varchar,
      bike_type varchar,
      start_time timestamp,
      start_station_id varchar,
      start_station_name varchar,
      end_station_id varchar,
      end_station_name varchar,
      duration_minutes integer
  )
  ```
- Import CSV data into table
  - Download this file first: https://raw.githubusercontent.com/yuda-notes/teaching-notes/refs/heads/main/dataset/bikeshare_trips.csv
  - Import CSV using pgAdmin

## Problem
- By using `psycopg2`
  - Select the data from `bikeshare_trips` with `duration_minutes` above 120 minutes and `bike_type` is electric.
  - Create a new table with the selected data called `filtered_bikeshare_trips`.
