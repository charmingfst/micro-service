#!/usr/bin/env bash
mvn package

docker build -t course-edge-service:latest .
