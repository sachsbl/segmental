# use this example script to push to DockerHub (or perhaps AWS ECR)

#!/usr/bin/env bash

docker login
docker build -t segmental .
docker tag paintly sachsbl/segmental:latest
docker push sachsbl/segmental:latest




