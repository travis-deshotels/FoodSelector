#!/usr/bin/bash

##############################################################
# Data file for the foodscript is provided via docker volume #
# Provide the host volume directory and name of the file     #
##############################################################

IMAGE_NAME=selector
HOST_VOLUME=$1
DATA_FILE=$2

if [ "$#" -ne 2 ]; then
    echo "Usage: docker-run.sh <HOST_VOLUME> <DATA_FILE>"
else
    docker run --name selector -v "${HOST_VOLUME}":/app/data "${IMAGE_NAME}" python foodscript.py data/"${DATA_FILE}"
fi
