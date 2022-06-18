import os
from google.cloud import bigquery
import json
import logging
from dotenv import load_dotenv
from fastapi import FastAPI

#Enable logging
load_dotenv()
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=LOGLEVEL,
    datefmt='%Y-%m-%d %H:%M:%S')


#################################################
# Author: Abhijit Kunjiraman
# Creation Date: 16-Jun-22
# Last Modified Date:17-Jun-22
# Change Logs:
# SL No         Date            Changes
# 1             17-Jun-22       Second Version
# 
#################################################
# Exit Codes:
# 101 - Cannot connect to Big Query Server
# 102 - Invalid User input
# 103 - No rows returned from big query
# 104 - Invalid SQL query
#################################################


def queries( n : int, year : int):

    """Gets and returns the aggregate statistics's of flights and records
    Parameters
    ----------
    state_short : str
        The short two-letter state and territory abbreviations
    Returns
    -------
    json
        1. Aggregate of count of planes based on status code
        2. Records of flight number, serial number, state name, status"""


    logging.info(f"Script Starts")
    if n in (0,1):
        logging.info(f"Value of n is valid, {n} is valid")
        if n==0:
            try:
                client = bigquery.Client()
                logging.info(f"Connection established to Big Query Server")
            except Exception as e:
                logging.error(f"Check the path of the JSON file and contents")
                logging.error(f"Cannot connect to Big Query Server")
                return 101
            try:
                logging.info(f"Querying data from big query for surveillance years")
                queryyears = client.query(f"""SELECT distinct extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
                left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
                where b.class = 'surveil' and extract(year from a.year_mfr) is not Null order by 1""")
            except Exception as e:
                logging.error(f"Bad SQL Query, verify SQL for fetching surveillance planes mfg years")
                return 104
            resultyear = queryyears.result()
            years=[]
            for mfgyear in resultyear:
                years.append(mfgyear[0])
            if year in years:
                try:
                    df = client.query(f"""SELECT * FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
                    left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
                    where b.class = 'surveil' and extract(year from a.year_mfr)={year}""").to_dataframe()
                except Exception as e:
                    logging.error(f"Bad SQL Query, verify SQL for fetching surveillance data")

                if df.empty:
                    logging.error(f"No rows returned from big query")
                    return 103

                logging.info(f"Parsing dataframe into Json object")
                json_records = df.to_json(orient='records')
                parsed_records = json.loads(json_records)
                json.dumps(json_records, indent=4)
                logging.info(f"Returning Json objects")
                return  parsed_records
            else:
                print('No non surrveilance planes were manufactured in the year provided please select from the following years ', years)
                return 105

        else:
            try:
                client = bigquery.Client()
                logging.info(f"Connection established to Big Query Server")
            except Exception as e:
                logging.error(f"Check the path of the JSON file and contents")
                logging.error(f"Cannot connect to Big Query Server")
                return 101
            try:
                logging.info(f"Querying data from big query for surveillance years")
                queryyears = client.query(f"""SELECT distinct extract(year from a.year_mfr) FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
                left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
                where b.class != 'surveil' and extract(year from a.year_mfr) is not Null order by 1""")
            except Exception as e:
                logging.error(f"Bad SQL Query, verify SQL for fetching years for non surveillance planes mfg years")
                return 104
            resultyear = queryyears.result()
            years=[]
            for mfgyear in resultyear:
                years.append(mfgyear[0])
            if year in years:
                try:
                    client = bigquery.Client()
                    logging.info(f"Connection established to Big Query Server")
                except Exception as e:
                    logging.error(f"Bad SQL Query, verify SQL for fetching surveillance data")

                try:
                    df = client.query(f"""SELECT * FROM `plane-detection-352701.SPY_PLANE.FAA_REGISTRATION-2022-06-13T00_09_43` a
                    left join `plane-detection-352701.SPY_PLANE.TRAIN` b on a.MODE_S_CODE_HEX=b.ADSHEX
                    where b.class != 'surveil' and extract(year from a.year_mfr)={year}""").to_dataframe()
                except Exception as e:
                    logging.error(f"Bad SQL Query, verify SQL for fetching surveillance data")

                if df.empty:
                    logging.error(f"No rows returned from big query")
                    return 103

                logging.info(f"Parsing dataframe into Json object")
                json_records = df.to_json(orient='records')
                parsed_records = json.loads(json_records)
                json.dumps(json_records, indent=4)
                logging.info(f"Returning Json objects")
                return  parsed_records
            else:
                print('No non surrveilance planes were manufactured in the year provided please select from the following years ', years)
                return 105
    else:
        print('please enter 0 for surveillance plane details or 1 for non-surveillance')
        return 106

def exit_script(error_code: int = 0):
    logging.info(f"Script Ends")
    exit(error_code)

def main( n : int, year : int):
    data = queries( n , year)
    if data in (101,102,103,104,105,106):
        exit_script(data)
    logging.debug("############## Printing Records          ##############")
    logging.debug(json.dumps(data[1][:5], indent=4, sort_keys=True))
    exit_script()

if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\abhij\Downloads\plane-detection-352701-90220d8b4de6.json"
    main(0,2000)