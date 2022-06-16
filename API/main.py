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

def query1(year: int):
    client = bigquery.Client()
    queryyears = client.query(f"""SELECT extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
    left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
    where b.class = 'surveil' and extract(year from a.year_mfr) is not Null""")
    resultyear = queryyears.result()
    years=[]
    for mfgyear in resultyear:
        years.append(mfgyear[0])
    if year in years:
        query_job = client.query(f"""SELECT * FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
        left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
        where b.class = 'surveil' and extract(year from a.year_mfr)={year}""")
        results = query_job.result()
        for row in results:
            print(row)
    else:
         print('No surrveilance planes were manufactured in the year provided please select from the following years ', years)


def main():
    query1(2010)


if __name__ == "__main__":
    main()