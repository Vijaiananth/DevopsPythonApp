# DevopsPythonApp
DevopsPythonApp

In this project, I have set up Devops for a simple Python app.

I have used CircleCI's 'aws-eks' ORB which creates and updates Kubernetes clusters easily for us in few steps:

https://circleci.com/developer/orbs/orb/circleci/aws-eks#usage-create-k8s-deployment

Rolling Deployment strategy is implemented in this where the Kubernetes cluster will be replaced with new changes completely during the deployment.

## Files and their purpose

1. app.py - Python app that returns predictions about housing prices
2. Dockerfile - File that creates Docker image
3. Makefile - Contains commands that sets up environment, runs tests and lints.
4. requirements.txt - Contains list of softwares to be installed in the environment.
5. Infra/infra.yml - contains configuration for the kubernetes cluster. Here the strategy specified is Rolling update and image pull is always.
6. Infra/service.yml - contains configuration for load balancer.

## Steps:

Circle CI will code will implement below steps:

1. Python app.py and Docker file will be linted.
2. Docker image will be prepared and pushed to Docker hub.
3. Kubernetes cluster and Load balancer will be created as per the config files.
4. Docker image will be deployed.
