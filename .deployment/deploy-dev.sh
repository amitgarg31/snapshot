#!/bin/bash

# Navigate to the dev deployment directory
cd ~/snapshot-dev

# Pull latest code
git pull origin dev

# Rebuild and restart the Docker containers
docker-compose down
docker-compose up --build -d
