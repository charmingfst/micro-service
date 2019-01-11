#!/usr/bin/env bash
mvn package
docker build -t course-service:latest .
