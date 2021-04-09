import json
import pandas as pd
import pathlib
import datetime

from modules import constant, app_element

def generate_dataframe():
    # Main DataFrame
    DATAFRAME_MAIN = pd.read_csv(constant.DATAFILE)
    DATAFRAME_MAIN.rename(constant.FIELD_MAP, axis=1, inplace=True)

    DATAFRAME_MAIN[constant.CREATED_DATE] = pd.to_datetime(DATAFRAME_MAIN[constant.CREATED_DATE], 
                                                   format = constant.DATE_FORMAT)
    DATAFRAME_MAIN[constant.CLOSED_DATE] = pd.to_datetime(DATAFRAME_MAIN[constant.CLOSED_DATE], 
                                                  format = constant.DATE_FORMAT)
    DATAFRAME_MAIN[constant.CREATED_DATE] =  DATAFRAME_MAIN[constant.CREATED_DATE].dt.date
    DATAFRAME_MAIN[constant.CLOSED_DATE] =  DATAFRAME_MAIN[constant.CLOSED_DATE].dt.date
    #Add Extra Column to identify Status Type OPEN/CLOSED
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status != @constant.CLOSED_ISSUE_STATUS'), constant.STATUS_TYPE] = "Open"
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status == @constant.CLOSED_ISSUE_STATUS'), constant.STATUS_TYPE] = "Closed"

    return(DATAFRAME_MAIN)

def get_open_issues(dataframe):
    return (dataframe.query('Status != @constant.CLOSED_ISSUE_STATUS'))

def get_closed_issues(dataframe):
    return (dataframe.query('Status == @constant.CLOSED_ISSUE_STATUS'))

def read_config_in_df():
    constant.read_config()  

    data = [
                ['identifier', constant.ISSUE_ID, constant.CSV_ISSUE_ID],
                ['status', constant.STATUS, constant.CSV_STATUS],
                ['reported_by', constant.REPORTED_BY, constant.CSV_REPORTED_BY],
                ['assigned_to', constant.ASSIGNED_TO, constant.CSV_ASSIGNED_TO],
                ['coded_by', constant.CODED_BY, constant.CSV_CODED_BY],
                ['severity', constant.SEVERITY, constant.CSV_SEVERITY],
                ['priority', constant.PRIORITY, constant.CSV_PRIORITY],
                ['customer', constant.CUSTOMER, constant.CSV_CUSTOMER],
                ['created_date', constant.CREATED_DATE, constant.CSV_CREATED_DATE],
                ['closed_date', constant.CLOSED_DATE, constant.CSV_CLOSED_DATE],
                ['issue_type', constant.ISSUE_TYPE, constant.CSV_ISSUE_TYPE]
            ]
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['FieldID', 'Field Name', 'Mapped To'])
    return (df)

def write_field_mapping_file(data,dt_format):
    JSON_FILE = {}
    JSON_FILE['KeyMapping'] = {}
    JSON_FILE['KeyMapping']['VarMapping'] = {}
    JSON_FILE['KeyMapping']['FieldMapping'] = {}

    for item in data:
        JSON_FILE['KeyMapping']['VarMapping'].update({item['FieldID'].rstrip(): item['Field Name'].rstrip()})
        JSON_FILE['KeyMapping']['FieldMapping'].update({item['Mapped To'].rstrip(): item['Field Name'].rstrip()})
    
    JSON_FILE["DateFormat"] = dt_format
    with open(constant.MAPPING_FILE, "w") as f:
        json.dump(JSON_FILE, f, indent = 3)
    
    return 0