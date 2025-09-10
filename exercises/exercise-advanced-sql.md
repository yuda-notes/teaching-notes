# Exercise Advanced SQL

## Setup
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
1. Tampilkan rata-rata `duration_minutes` dari setiap subscriber_type.
   - Contoh output: <br>
     <img width="452" height="407" alt="image" src="https://github.com/user-attachments/assets/9208183b-4772-4016-a851-256e8590c625" />

2. Tampilkan ranking berdasarkan durasi terlama di setiap `subscriber_type`.
   - Contoh output: <br>
     <img width="494" height="407" alt="image" src="https://github.com/user-attachments/assets/e2eeec81-061c-4df8-8eb6-543407f7cd3f" />

3. Tampilkan rata-rata `duration_minutes` berdasarkan `bike_type` sesuai dengan output berikut:
   - Contoh output: <br>
     <img width="352" height="79" alt="image" src="https://github.com/user-attachments/assets/f8dc7bf3-c8dd-456f-a52d-9f1014176a62" />
