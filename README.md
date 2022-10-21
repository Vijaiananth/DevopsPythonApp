# DevopsPythonApp
DevopsPythonApp

In this project, I have set up Devops for a simple Python app.





## Files and their purpose

1. app.py - Python app that returns predictions about housing prices
2. Dockerfile - File that creates Docker image
3. Makefile - Contains commands that sets up environment, runs tests and lints.
4. requirements.txt - Contains list of softwares to be installed in the environment.
5. make_prediction.sh - sends api request to the running app and gets prediction response.
6. run_docker.sh - script to build and run docker image
7. upload_docker.sh - script to upload docker image to docker hub
8. run_kubernetes.sh - script to set up app and run it on kubernetes cluster