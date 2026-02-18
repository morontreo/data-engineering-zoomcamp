# Queries

# Question 3:
dbt show --inline "select count(*) from {{ref('fct_monthly_zone_revenue')}}" --target prod

# Question 4:
dbt show --target prod --inline "
SELECT 
    pickup_zone, 
    SUM(revenue_monthly_total_amount) as total_rev 
FROM {{ ref('fct_monthly_zone_revenue') }}
WHERE 
    service_type = 'Green' 
    AND extract(year from revenue_month) = 2020 
GROUP BY 1 
ORDER BY total_rev DESC"

# Question 5:
dbt show --target prod --inline "
SELECT 
    SUM(total_monthly_trips) as total_trips
FROM {{ ref('fct_monthly_zone_revenue') }}
WHERE 
    service_type = 'Green' 
    AND extract(year from revenue_month) = 2019
    AND extract(month from revenue_month) = 10
"

# Question 6:
dbt --target prod --inline "select count(*) from {{ref('stg_fhv_tripdata')}}"