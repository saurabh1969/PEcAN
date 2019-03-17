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
## Running App using Docker


## Build Docker

``` shell
docker build -t pecan-docker:latest . 
```

## Run Docker image

``` shell
docker run -d -p 5000:5000 pecan-docker
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

## Uploading the CSV
 1. Put the csv into app folder
 2. While uploading the CSV,write name of the file with extension(.csv)

## License

This project is licensed under the MIT open source license.
