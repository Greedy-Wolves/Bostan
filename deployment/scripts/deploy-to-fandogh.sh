#!/bin/bash
set -e

curl -s https://api.github.com/repos/Greedy-Wolves/Bostan-UI/releases/latest \
| jq -r '.assets[].browser_download_url' \
| wget -qi -
tar xzf dist.tar.gz

COLLECT_ERROR=True fandogh login --username=$FAN_USR --password=$FAN_PASS
fandogh image init --name=bostan_backend
fandogh image publish --version=$TRAVIS_COMMIT
fandogh service deploy --version=$TRAVIS_COMMIT --name=bostan
