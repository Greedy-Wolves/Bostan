#!/bin/bash
COLLECT_ERROR=True fandogh login --username $FAN_USR --password $FAN_PASS
fandogh image init --name=bostan_backend
fandogh image publish --version=$TRAVIS_COMMIT