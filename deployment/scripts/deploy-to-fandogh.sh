#!/bin/bash
pip install fandogh_cli --upgrade
fandogh login --username $FAN_USR --password $FAN_PASS
fandogh image init --name=bostan_backend
fandogh image publish --version `printf "v0.%03d" ${TRAVIS_BUILD_NUMBER}`

echo "TRAVIS_BUILD_NUMBER: ${TRAVIS_BUILD_NUMBER}"
echo "TRAVIS_JOB_NUMBER: ${TRAVIS_JOB_NUMBER}"