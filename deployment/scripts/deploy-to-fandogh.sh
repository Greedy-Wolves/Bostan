#!/bin/bash

curl -s https://api.github.com/repos/Greedy-Wolves/Bostan-UI/releases/latest \
| grep "dist.tar.gz" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -
tar xzf dist.tar.gz

COLLECT_ERROR=True fandogh login --username=$FAN_USR --password=$FAN_PASS
fandogh image init --name=bostan_backend
fandogh image publish --version=$TRAVIS_COMMIT
fandogh service deploy --version=$TRAVIS_COMMIT --name=bostan
