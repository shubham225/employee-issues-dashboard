# employee-issues-dashboard
A Web Dashboard for Employee Issues, Created with Plotly Dash

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project is build using python 3, if not installed you can download it from [python.org](https://www.python.org/downloads/).

Need to install following python modules before running this project. execute following commands to install them

```
pip install dash
pip install dash_auth
pip install dash_bootstrap_components
```

### Installing

To install the project clone repository to local machine or download zip of the repository.

## Running the Project

After getting project directory on local machine project can be run by following command

```
	python index.py                 #on windows
	python3 index.py                #on linux if old python installation has been kept for backward compatibility 
```

./datasets folder contains a sample .csv file which is used as datasource in current scenario.
this file can be updated periodically to display latest data to the dashboard.
updating csv file from remote SQL server/datasource will be added in next revisions.

## Overview of app pages

### Home
This page will have graphs and charts of the employee tickets analytics.

![alt text](https://github.com/shubham225/kali-gnome-menu-fix/blob/main/docs/imgs/homepage.png)

### Overview

This page will have detailed information in tabular format and can have no. of critial issues.

![alt text](https://github.com/shubham225/kali-gnome-menu-fix/blob/main/docs/imgs/overview.png)

### Settings
This page contains the setup related part of the application, currently it has mapping table which is used top map the excel sheet columns to application specific fields and date format related info of the dataset sheet.

![alt text](https://github.com/shubham225/kali-gnome-menu-fix/blob/main/docs/imgs/settings.png)

This option will include advanced options such as datasource setup and user login management.


## Built With

* [Plotly-dash](https://dash.plotly.com/introduction) - Python framework for building web analytic applications
* [Dash-Bootstrap-Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/) - Component library for use with Plotly Dash


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
