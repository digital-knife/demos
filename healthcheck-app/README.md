# Healthcheck App Demo
Python API with Ansible deployment.

## Setup
cd ansible
ansible-playbook deploy.yml

## Run
docker build -t healthcheck-app .
docker run -p 5000:5000 healthcheck-app
