# Selenium on docker framework

# Usage

## Prepare services
```
$ cd docker
$ docker-compose up -d
$ docker-compose run web bower install
```

## Connect to share desktop (If need)
Finder >> move >> connect server
* Server address: `vnc://0.0.0.0:5900`
* password: `secret`


## Run testing
```
$ docker-compose run main python test/main.py
```

## Stop services
```
$ docker-compose stop
```


# For developing

## Install new js libraries to web for testing
```
$ docker-compose run web bower install jquery --save
```
