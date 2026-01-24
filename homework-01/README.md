# QUERIES:

**Question 3:**
--- 
<pre>
SELECT count(*) 
FROM green_tripdata 
WHERE lpep_pickup_datetime >= '2025-11-01 00:00:00' 
AND lpep_pickup_datetime < '2025-12-01 00:00:00' 
AND trip_distance <=1 
</pre>

**Question 4:**
--- 
SELECT 
    lpep_pickup_datetime::date AS pickup_day,
    MAX(trip_distance) AS max_trip_distance
FROM green_tripdata
WHERE lpep_pickup_datetime::date IN ('2025-11-14', '2025-11-20', '2025-11-23', '2025-11-25')
  AND trip_distance < 100
GROUP BY pickup_day
ORDER BY pickup_day;

**Question 5:**
---
SELECT g."PULocationID", count(*) as total_amount, t."Zone"
FROM green_tripdata g, taxi_zone_lookup t
WHERE g."PULocationID" = t."LocationID"
GROUP BY g."PULocationID",t."Zone"
ORDER BY total_amount DESC;

**Question 6:**
---
SELECT 
    MAX(g.tip_amount) AS max_tip_amount, 
    d."Zone" 
FROM green_tripdata g
JOIN taxi_zone_lookup p ON g."PULocationID" = p."LocationID"
JOIN taxi_zone_lookup d ON g."DOLocationID" = d."LocationID"
WHERE p."Zone" = 'East Harlem North'
GROUP BY d."Zone"
ORDER BY max_tip_amount DESC;