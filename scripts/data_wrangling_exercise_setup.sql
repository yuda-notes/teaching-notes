-- create new table
create table trips(
	trip_id int primary key,
	subscriber_type varchar,
	bike_id varchar,
	bike_type varchar,
	start_time date,
	start_station_id int,
	start_station_name varchar,
	end_station_id int,
	end_station_name varchar,
	duration_minutes int
);

-- import data from csv into table
COPY trips(trip_id,subscriber_type,bike_id,bike_type,start_time,start_station_id,start_station_name,end_station_id,end_station_name,duration_minutes)
-- change the directory based on your system, comment the unused line.
FROM 'C:\your\path\to\file.csv' -- for Windows
FROM '/your/path/to/file.csv' -- for Mac/Linux
DELIMITER ','
CSV HEADER;