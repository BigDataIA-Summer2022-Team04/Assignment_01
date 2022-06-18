import os
from google.cloud import bigquery
import json
import logging
from dotenv import load_dotenv
from fastapi import FastAPI

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


def noofflights(quan: int,flights: int):
    if quan in (0,1):
        if quan == 1:
            client = bigquery.Client()
            query_job = client.query(f"""SELECT adshex, flights, type FROM `plane-detection-352701.SPY_PLANE.PLANE_FEATURES` 
            where flights > {flights} order by flights desc""")
            results = query_job.result()  # Waits for job to complete.
            for row in results:
                print(f"{row}")
        else:
            client = bigquery.Client()
            query_job = client.query(f"""SELECT adshex, flights, type FROM `plane-detection-352701.SPY_PLANE.PLANE_FEATURES` 
            where flights < {flights} order by flights desc""")
            results = query_job.result()  # Waits for job to complete.
            for row in results:
                print(f"{row}")


def query2(year: int):
    client = bigquery.Client()
    queryyears = client.query(f"""SELECT distinct extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
    left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
    where b.class != 'surveil' and extract(year from a.year_mfr) is not Null order by 1""")
    resultyear = queryyears.result()
    years=[]
    for mfgyear in resultyear:
        years.append(mfgyear[0])
    if year in years:
        query_job = client.query(f"""SELECT * FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
        left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
        where b.class != 'surveil' and extract(year from a.year_mfr)={year}""")
        results = query_job.result()
        for row in results:
            print(row)
    else:
         print('No non surrveilance planes were manufactured in the year provided please select from the following years ', years)

def queries( n : int, year : int):
    if n in (0,1):
        if n==0:
            client = bigquery.Client()
            queryyears = client.query(f"""SELECT distinct extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
            left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
            where b.class = 'surveil' and extract(year from a.year_mfr) is not Null order by 1""")
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
        else:
            client = bigquery.Client()
            queryyears = client.query(f"""SELECT distinct extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
            left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
            where b.class != 'surveil' and extract(year from a.year_mfr) is not Null order by 1""")
            resultyear = queryyears.result()
            years=[]
            for mfgyear in resultyear:
                years.append(mfgyear[0])
            if year in years:
                query_job = client.query(f"""SELECT * FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
                left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
                where b.class != 'surveil' and extract(year from a.year_mfr)={year}""")
                results = query_job.result()
                for row in results:
                    print(row)
            else:
                print('No non surrveilance planes were manufactured in the year provided please select from the following years ', years)
    else:
        print('please enter 0 for surveillance plane details or 1 for non-surveillance')


def typeaircraft(type:int):
    client = bigquery.Client()
    aircrafttypes = client.query(f"""select distinct TYPE_AIRCRAFT from `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` order by 1""")
    resulttype = aircrafttypes.result()
    listypes=[]
    for row in resulttype:
        listypes.append(row[0])
    if type in listypes:
        query_job = client.query(f"""SELECT N_NUMBER, SERIAL_NUMBER, NAME, MFR_MDL_CODE, ENG_MFR_MDL, TYPE_AIRCRAFT, TYPE_ENGINE FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` 
        where TYPE_AIRCRAFT={type}""")
        results = query_job.result()
        for row in results:
            print(row)
    else:
         print('Please enter a valid aircraft type from this list ', listypes)

def typengine(type:int):
    client = bigquery.Client()
    aircrafttypes = client.query(f"""select distinct TYPE_ENGINE from `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` order by 1""")
    resulttype = aircrafttypes.result()
    listypes=[]
    for row in resulttype:
        listypes.append(row[0])
    if type in listypes:
        query_job = client.query(f"""SELECT N_NUMBER, SERIAL_NUMBER, NAME, MFR_MDL_CODE, ENG_MFR_MDL, TYPE_AIRCRAFT, TYPE_ENGINE FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` 
        where TYPE_ENGINE={type}""")
        results = query_job.result()
        for row in results:
            print(row)
    else:
         print('Please enter a valid aircraft type from this list ', listypes)





def main():
    """queries(1,200)
    typeaircraft(100)
    typengine(100)"""
    noofflights(1, 1000)


if __name__ == "__main__":
    main()