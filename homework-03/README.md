# Queries

# Question 2:

## External Table:
SELECT DISTINCT PULocationID FROM `de-homework03.dehwk03.yellow_taxi_trip_ext`
This query will process 0B

## Materialized Table:
SELECT DISTINCT PULocationID FROM `de-homework03.dehwk03.yellow_taxi_trip_mat`
This query will process 155.12MB

# Question 3:
SELECT PULocationID FROM `de-homework03.dehwk03.yellow_taxi_trip_mat`
SELECT PULocationID, DOLocationID FROM `de-homework03.dehwk03.yellow_taxi_trip_mat`

# Question 4:
SELECT count(*) FROM `de-homework03.dehwk03.yellow_taxi_trip_ext` WHERE fare_amount = 0
This query will return 8,333

# Question 6:

## Partitioning the table
CREATE TABLE `de-homework03.dehwk03.yellow_taxi_trip_mpc`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `de-homework03.dehwk03.yellow_taxi_trip_ext`;

## Query Materialized non-partitioned/non-clustered table (mat)
SELECT DISTINCT
  VendorID
FROM
  `de-homework03.dehwk03.yellow_taxi_trip_mat`
WHERE
  tpep_dropoff_datetime >= '2024-03-01'
  AND tpep_dropoff_datetime <= '2024-03-15';
This query will process 310.24MB

## Query Materialized partitioned/clustered table (mpc)
SELECT DISTINCT
  VendorID
FROM
  `de-homework03.dehwk03.yellow_taxi_trip_mpc`
WHERE
  tpep_dropoff_datetime >= '2024-03-01'
  AND tpep_dropoff_datetime <= '2024-03-15';
This query will process 26.84MB

