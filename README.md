# dumbfucks-club

## Architecture Diagram
// TODO make this thing

## Cloudflare Tunnel Setup
// TODO fill this in

## Running www
1. docker build . -t personal-site
2. docker run -d -p 8000:8000 --name personal-site personal-site

## Running wiki

1. generate an app key (run dockerfile with empty app_key and program will inform how to generate)
2. move appropriate env file into same dir as docker-compose file and rename to just .env
3. update any secure values in the env file that wouldn't be pushed to docker
4. run `docker compose up --build -d`

## Running dnd
1. get a timed url from foundryvtt for linux
2. run `docker compose up --build -d`

