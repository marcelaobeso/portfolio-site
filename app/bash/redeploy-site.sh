#!/bin/bash

cd /root/portfolio-site
git fetch && git reset origin/main --hards
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
