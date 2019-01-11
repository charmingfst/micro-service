#!/usr/bin/env bash
mvn package

docker build -t api-gateway-zuul:latest .
