
PREPARATION: Create Table
---------------------------------------------------------
CREATE TABLE processed_events (
    lpep_pickup_datetime TIMESTAMP,
    lpep_dropoff_datetime TIMESTAMP,
    PULocationID INTEGER,
    DOLocationID INTEGER,
    passenger_count INTEGER,
    trip_distance DOUBLE PRECISION,
    tip_amount DOUBLE PRECISION,
    total_amount DOUBLE PRECISION  
);


QUESTION 3:
------------------------------
select count(*) from processed_events where trip_distance > 5