# qna-app
qna app built using Flask and MySQL

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="94" height="20" role="img" aria-label="python: 3.10.6"><title>python: 3.10.6</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="94" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="49" height="20" fill="#555"/><rect x="49" width="45" height="20" fill="#97ca00"/><rect width="94" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="255" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="390">python</text><text x="255" y="140" transform="scale(.1)" fill="#fff" textLength="390">python</text><text aria-hidden="true" x="705" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="350">3.10.6</text><text x="705" y="140" transform="scale(.1)" fill="#fff" textLength="350">3.10.6</text></g></svg>

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
