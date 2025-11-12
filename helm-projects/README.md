# Helm Minikube Demo
Deploys status-page via Helm on Minikube.

## Setup
./get_helm.sh
minikube start --driver=docker
helm install status-page ./status-page --set service.type=NodePort

## Verify
minikube service status-page --url | xargs curl

### After Reboot (Jenkins crash fix)
```bash
minikube start --driver=docker
./helm-projects/deploy-jenkins.sh
