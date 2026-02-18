with source as (
        select * from {{ source('raw', 'fhv_tripdata') }}
        where dispatching_base_num is not null
  ),
  renamed as (
      select
          {{ adapter.quote("dispatching_base_num") }},
        {{ adapter.quote("pickup_datetime") }},
        {{ adapter.quote("dropOff_datetime") }},
        {{ adapter.quote("PUlocationID") }}  as pickup_location_id,
        {{ adapter.quote("DOlocationID") }} as dropoff_location_id,
        {{ adapter.quote("SR_Flag") }},
        {{ adapter.quote("Affiliated_base_number") }}
      from source
  )
  select * from renamed
