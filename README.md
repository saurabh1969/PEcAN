PEcAN App
======================
Meta-Data Upload Interface


### Description
This is simple counter application, using flask microframework and sqlite3 to load the metadata csv to SQLIte database.

### Install guide

## Clone the repo

```bash
git clone https://github.com/saurabh1969/PEcAN.git
```

## Running App Local

## Go to app folder

```bash
cd app
```

## Create the virtualenv
```bash
mkvirtualenv app
```

## Install dependencies
```shell
pip install -r requirements.txt
```

## Run the app
```shell
python routes.py
```

## Endpoints:

 1. Uploading the csv : curl -X POST http://127.0.0.1:5000/insert?file=switchgrass.csv 

 2. Searching:         curl -X POST http://127.0.0.1:5000/search?id=4

## License

This project is licensed under the MIT open source license.
