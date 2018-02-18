#!/bin/bash

# Cleanup:
docker rm -f selenium-hub
docker rm -f selenium-node-chrome
docker rm -f selenium-node-firefox

# Running:
docker run -d -p 4444:4444 --name selenium-hub selenium/hub:3.8.1-francium

docker run -d --link selenium-hub:hub --name selenium-node-chrome -v /dev/shm:/dev/shm selenium/node-chrome:3.8.1-francium

docker run -d --link selenium-hub:hub --name selenium-node-firefox -v /dev/shm:/dev/shm selenium/node-firefox:3.8.1-francium
