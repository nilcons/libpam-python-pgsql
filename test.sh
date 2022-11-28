#!/bin/bash

set -eu
set -o pipefail

# python2
docker build -f test.Dockerfile-buster --build-arg CACHEBUST=$(date +%s) .

# python3
docker build -f test.Dockerfile-bullseye --build-arg CACHEBUST=$(date +%s) .
