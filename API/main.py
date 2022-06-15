import os
from fastapi import FastAPI
from google.cloud import bigquery

app = FastAPI()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\abhij\Downloads\plane-detection-352701-90220d8b4de6.json"


def query():
    client = bigquery.Client()
    query_job = client.query(
        """
        WITH
        CTE AS (
        SELECT
            *
        FROM
            `plane-detection-352701.SPY_PLANE.FAA`
        WHERE
            YEAR_MFR IS NOT NULL )
        SELECT
        EXTRACT(YEAR
        FROM
            YEAR_MFR) AS YEARS_REGISTERED,
        COUNT(*) AS COUNT_OF_FLIGHTS
        FROM
        CTE
        GROUP BY
        YEARS_REGISTERED
        ORDER BY
        2 DESC,
        YEARS_REGISTERED
        NULLS LAST
        LIMIT
        5
        """
    )

    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print("{} : {}".format(row.YEARS_REGISTERED, row.COUNT_OF_FLIGHTS))


def test_dynamic(row_counts: int):
    client = bigquery.Client()
    query_job = client.query(f"SELECT YEAR_MFR FROM `plane-detection-352701.SPY_PLANE.FAA` LIMIT {row_counts}")
    results = query_job.result()  # Waits for job to complete.
    for row in results:
        print(f"{row}")


def main():
    query()


if __name__ == "__main__":
    main()