#!/usr/bin/env bash
mvn package

docker build -t user-edge-service:latest .

# docker run -it user-edge-service:latest --redis.address=192.168.1.7