import pytest
import os
from dotenv import load_dotenv
from mfgplanesinfo import queries
from n_of_flights import noofflights
from typeaircraft import typeaircraft
from typeengine import typengine



#################################################
# Author: Abhijit Kunjiraman
# Creation Date: 17-Jun-22
# Last Modified Date:
# Change Logs:
# SL No         Date            Changes
# 1             17-Jun-22       First Version
# 
#################################################

load_dotenv()




## Incorrect Big Query JSON KEY
def test_incorrect_json_file_mfgplanesinfo():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert queries(0,2000) == 101

def test_incorrect_json_file_n_of_flights():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert noofflights(0,900) == 101

def test_incorrect_json_file_type_engine():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert typengine(1) == 101

def test_incorrect_json_file_type_registrant():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert typeaircraft('MA') == 101


## Data Found from Big Query

def test_incorrect_type_aircraft():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    assert typeaircraft(100) == 102

def test_incorrecttype_engine():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    assert typengine(90) == 102

def test_incorrect_mfgplanesinfo_year():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    assert queries(1,1900)== 103
