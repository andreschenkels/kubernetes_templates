# Setup

## python
Use python 3.6.6,
```
virtualenv .env
. .env/bin/activate
```

## Flask
```
pip install -r requirements.txt
```

## Run in dev environment
```
FLASK_ENV=development FLASK_APP=app.py flask run
```

## Docker
```
docker build -t <REGISTRY>/<REPOSITORY>:<TAG>
docker run -p 5000:5000 <REGISTRY>/<REPOSITORY>:<TAG>
```
