"""NYC taxi data pipeline from REST API."""

import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator


@dlt.resource(name="rides", write_disposition="replace")
def taxi_rides():
    """Fetch taxi rides (1,000 per page, stop when empty page)."""
    client = RESTClient(
        base_url="https://us-central1-dlthub-analytics.cloudfunctions.net",
        paginator=PageNumberPaginator(
            base_page=1,
            page_param="page",
            total_path=None,
            stop_after_empty_page=True,
        ),
    )

    for page in client.paginate("/data_engineering_zoomcamp_api"):
        yield page
        print(f"Fetched {len(page)} records")


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    dataset_name="taxi_data",
)

if __name__ == "__main__":
    print("Starting pipeline...")
    load_info = pipeline.run(taxi_rides())
    print("Pipeline finished!")
    print(load_info)
