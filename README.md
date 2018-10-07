# Kubernetes Templates

Templates for a Hello World app with
* a React frontend served by a Nginx webserver
* connected to a Flask API served by uWSGI and Nginx
* powered by a MySQL database
* with an Adminer role to visualise data.

## app - The React app
A Docker registry is needed to push the docker image.
Nothing to be changed for the app to run.

## api - The Flask API
A Docker registry is needed to push the docker image.
The MySQL database name must be provided in `conf.py` in place of `<DATABASE>`.

## deploy - kubernetes deployments & services
* Secrets must be created and base64 encoded.
* Node Ports for `app`, `api` and `adminer` services must be specified in place of `<PORT>`.
* Docker image names must be provided for `api` and `app` deployments.
* app config files need the IP/host name and port of the API role in place of `<HOSTNAME>:<PORT>`.
* First time the `mysql` deployment is created, the appropriate user(s) and database(s) have to be manually created, see `deploy/README.md`.
