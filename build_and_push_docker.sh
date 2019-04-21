# use this example script to push to DockerHub (or perhaps AWS ECR)

#!/usr/bin/env bash

docker login
docker build -t segmental .
docker tag paintly sachsbl/segmental:latest
docker push sachsbl/segmental:latest

$(aws ecr get-login --no-include-email --region us-east-1)
docker tag segmental:latest 116226363472.dkr.ecr.us-east-1.amazonaws.com/segmental:latest
docker push 116226363472.dkr.ecr.us-east-1.amazonaws.com/segmental:latest



