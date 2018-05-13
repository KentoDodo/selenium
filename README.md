# Selenium on docker framework

# Usage

## Prepare services
```
$ docker-compose up -d
```

## Connect to share desktop
Finder >> move >> connect server
* Server address: `vnc://0.0.0.0:5900`
* password: `secret`


## Run testing
```
$ docker-compose run main python command/test.py
```

## Stop services
```
$ docker-compose stop
```
