#!/usr/bin/bash
echo $'\nFetching changes from remote repository\n'

FETCH=$(cd ~/portfolio-site && git fetch && git reset origin/main --hard)
echo "$FETCH"

echo $'\n\nRemoving Containers\n'
DOWN=$(docker compose -f docker-compose.prod.yaml down)

echo "$DOWN"


echo $'\nStarting containers up\n'
BUILD=$(docker compose -f docker-compose.prod.yaml up -d --force-recreate)

echo "$BUILD"
