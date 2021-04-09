import json

APP_LOGO = "images/plotly-logomark.png"
MAPPING_FILE = "config/fields_mapping.json"
DATAFILE = "datasets/sample-employee-issues-data.csv"

# save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'shubham': 'login123'
}

# the style arguments for the sidebar. 
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "0rem 0rem",
    "background-color": "dark"
}

NAVITEM_STYLE = {
    "padding": "0rem 1rem"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "15rem",
    "padding": "0rem 0rem"
}

# Initialize with default values
ISSUE_ID = "Issue ID"
STATUS = "Status"
REPORTED_BY = "Reported By"
ASSIGNED_TO = "Assigned To"
CODED_BY = "Coded By"
SEVERITY = "Severity"
PRIORITY = "Priority"
CUSTOMER = "Customer"
CREATED_DATE = "Created Date"
CLOSED_DATE = "Closed Date"
ISSUE_TYPE = "Issue Type"

CSV_ISSUE_ID = "Issue ID"
CSV_STATUS = "Status"
CSV_REPORTED_BY = "Reported By"
CSV_ASSIGNED_TO = "Assigned To"
CSV_CODED_BY = "Coded By"
CSV_SEVERITY = "Severity"
CSV_PRIORITY = "Priority"
CSV_CUSTOMER = "Customer"
CSV_CREATED_DATE = "Created Date"
CSV_CLOSED_DATE = "Closed Date"
CSV_ISSUE_TYPE = "Issue Type"

FIELD_MAP = {
    "Issue ID": "Issue ID",
    "Status": "Status",
    "Reported By": "Reported By",
    "Assigned To": "Assigned To",
    "Coded By": "Coded By",
    "Severity": "Severity",
    "Priority": "Priority",
    "Customer": "Customer",
    "Created Date": "Created Date",
    "Closed Date": "Closed Date",
    "Issue Type": "Issue Type"
}
DATE_FORMAT = "%d-%m-%Y %H:%M"

# Custom Variables
CREATED_TIME = 'CreatedTime'
CREATED_DT = 'CreatedDT'
STATUS_TYPE = 'StatusType'
CLOSED_ISSUE_STATUS = ["Closed", "Weekend Solution - IS", "Solution Proposed","Resolved", "Solution Loaded", "Solution Documented"]


def read_config():
    global ISSUE_ID
    global STATUS
    global REPORTED_BY
    global ASSIGNED_TO
    global CODED_BY
    global SEVERITY
    global PRIORITY
    global CUSTOMER
    global CREATED_DATE
    global CLOSED_DATE
    global ISSUE_TYPE

    global CSV_ISSUE_ID
    global CSV_STATUS
    global CSV_REPORTED_BY
    global CSV_ASSIGNED_TO
    global CSV_CODED_BY
    global CSV_SEVERITY
    global CSV_PRIORITY
    global CSV_CUSTOMER
    global CSV_CREATED_DATE
    global CSV_CLOSED_DATE
    global CSV_ISSUE_TYPE

    global FIELD_MAP
    global DATE_FORMAT

    with open(MAPPING_FILE) as f:
        CONFIG_OBJECT = json.load(f)

    FIELD_MAP    = CONFIG_OBJECT["KeyMapping"]["FieldMapping"]
    ISSUE_ID     = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["identifier"]
    STATUS       = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["status"]
    REPORTED_BY  = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["reported_by"]
    ASSIGNED_TO  = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["assigned_to"]
    CODED_BY     = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["coded_by"]
    SEVERITY     = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["severity"]
    PRIORITY     = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["priority"]
    CUSTOMER     = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["customer"]
    CREATED_DATE = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["created_date"]
    CLOSED_DATE  = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["closed_date"]
    ISSUE_TYPE   = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["issue_type"]
    DATE_FORMAT  = CONFIG_OBJECT["DateFormat"]

    key_list = list(FIELD_MAP.keys())
    val_list = list(FIELD_MAP.values())   
    
    CSV_ISSUE_ID = key_list[val_list.index(ISSUE_ID)]
    CSV_STATUS = key_list[val_list.index(STATUS)]
    CSV_REPORTED_BY = key_list[val_list.index(REPORTED_BY)]
    CSV_ASSIGNED_TO = key_list[val_list.index(ASSIGNED_TO)]
    CSV_CODED_BY = key_list[val_list.index(CODED_BY)]
    CSV_SEVERITY = key_list[val_list.index(SEVERITY)]
    CSV_PRIORITY = key_list[val_list.index(PRIORITY)]
    CSV_CUSTOMER = key_list[val_list.index(CUSTOMER)]
    CSV_CREATED_DATE = key_list[val_list.index(CREATED_DATE)]
    CSV_CLOSED_DATE = key_list[val_list.index(CLOSED_DATE)]
    CSV_ISSUE_TYPE = key_list[val_list.index(ISSUE_TYPE)]
 