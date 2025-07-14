#!/bin/bash

TARGET_ID=$(curl http://radnitz-oriasotie.duckdns.org:5000/api/timeline_post | jq  '.[] | .[0] | .id') #GET ID OF MOST RECENT POST (PYTHON SORTS GET BY INVERSE OF TIME CREATED)
TARGET_ID=$(($TARGET_ID+1)) #TARGET ID IS +1 OF CURRENT HIGHEST ID 

curl -X POST http://radnitz-oriasotie.duckdns.org:5000/api/timeline_post -d 'name=Radnitz&email=oriasotr@tcd.ie&content=Random Post' #POST RANDOM POST

HIGHEST_ID=$(curl http://radnitz-oriasotie.duckdns.org:5000/api/timeline_post | jq  '.[] | .[0] | .id') #CHECK NEW HIGHEST ID

if [[ $HIGHEST_ID -ge $TARGET_ID ]]; then 
	echo "ADDED"
	exit 0 
fi
echo "ERROR"
>&2 echo "The POST was not added"
exit 1

