echo off
set IMAGE_NAME=selector
set HOST_VOLUME=%1
set DATA_FILE=%2

REM ##############################################################
REM # Data file for the foodscript is provided via docker volume #
REM # Provide the host volume directory and name of the file     #
REM ##############################################################

set argC=0
for %%x in (%*) do Set /A argC+=1

if %argC% LSS 2 (
    echo "Usage: docker-run.cmd <HOST_VOLUME> <DATA_FILE>"
) else (
    docker run --name selector -v %HOST_VOLUME%:/app/data %IMAGE_NAME% python foodscript.py data/%DATA_FILE%
)
