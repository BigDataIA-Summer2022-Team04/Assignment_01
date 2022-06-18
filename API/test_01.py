import pytest
import os
from dotenv import load_dotenv
from validate_state import validate_state
from status_code import status_code
from type_engine import type_engine
from type_registrant import type_registrant
from type_aircraft import type_aircraft

#################################################
# Author: Piyush
# Creation Date: 17-Jun-22
# Last Modified Date:
# Change Logs:
# SL No         Date            Changes
# 1             17-Jun-22       First Version
# 
#################################################

load_dotenv()

## Invalid State Name
def test_state_uppercase():
    assert validate_state('MA') == True

def test_state_lowercase():
    assert validate_state('ma') == True

def test_invalid_state():
    assert validate_state('none') == False


## Incorrect Big Query JSON KEY
def test_incorrect_json_file_status_code():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert status_code('MA') == 101

def test_incorrect_json_file_type_aircraft():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert type_aircraft('MA') == 101

def test_incorrect_json_file_type_engine():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert type_engine('MA') == 101

def test_incorrect_json_file_type_registrant():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON_INVALID')
    assert type_registrant('MA') == 101


## Incorrect Sate Abbreviations
def test_incorrect_state_name_status_code():
    assert status_code('NO_State') == 102

def test_incorrect_state_name_type_aircraft():
    assert type_aircraft('NO_State') == 102

def test_incorrect_state_name_type_engine():
    assert type_engine('NO_State') == 102

def test_incorrect_state_name_type_registrant():
    assert type_registrant('NO_State') == 102


## Data Found from Big Query
def test_incorrect_state_name_status_code():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    returns = status_code('MA')
    assert len(returns) == 2

def test_incorrect_state_name_type_aircraft():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    returns = type_aircraft('MA')
    assert len(returns) == 2

def test_incorrect_state_name_type_engine():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    returns = type_engine('MA')
    assert len(returns) == 2

def test_incorrect_state_name_type_registrant():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('BQ_KEY_JSON')
    returns = type_registrant('MA')
    assert len(returns) == 2