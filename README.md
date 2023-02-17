# qna-app
qna app built using Flask and MySQL

![Python](https://shields.io/static/v1?label=python&message=3.10.6&color=green) ![Flask](https://shields.io/static/v1?label=flask&message=2.2.2&color=green)

## Prerequisites
Before you start using the app, you need to have the following installed on your machine:

- Python 3
- Flask
- MySQL


## Installation

1.Clone the repository

`git clone https://github.com/pj8912/qna-app.git`

2.Create a virtual environment
`python3 -m venv env`

`source env/bin/activate`


3.Install the requirements
`pip install -r requirements.txt`

4.Create .env file and add values for the following

- DB_HOST=YOUR_DB_HOST
- DB_USERNAME=YOUR_DB_USERNAME
- DB_PWD=YOUR_PWD
- DB_NAME=YOUR_DB_NAME
- APP_NAME=YOUR_APP_NAME

5.Export sql file from `sql/qna.sql`


6.Run app

`python app.py`


## Features
- User authentication (sign up and log in)
- Ask questions
- Answer questions
- View questions and answers

## Contributors

- [jp](https://github.com/pj8912)
