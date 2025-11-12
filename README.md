# Demos Repo
Collection of SRE/DevOps demos.

## Demos
- [Helm Projects](./helm-projects): K8s status-page with Helm, Prometheus monitoring, Grafana dashboard, and Jenkins CI/CD pipeline.
- [Healthcheck App](./healthcheck-app): Python API + Ansible deployment.
- [Postman Tests](./postman-tests): API testing collections.

## Run a Demo
git clone https://github.com/digital-knife/demos.git -b jenkins-integration
cd demos/helm-projects && ./get_helm.sh

### Helm Status-Page Setup
1. Install Helm: `./get_helm.sh`.
2. Start Minikube: `minikube start --driver=docker`.
3. Deploy: `helm install status-page ./status-page --set service.type=NodePort`.
4. Access: `minikube service status-page --url` → curl / for JSON health.
5. Toggle internal: `helm upgrade status-page ./status-page --set service.type=ClusterIP`.

### Prometheus Monitoring
helm install prometheus-stack prometheus-community/kube-prometheus-stack -f prometheus-custom-values.yaml --namespace monitoring --create-namespace
kubectl port-forward -n monitoring svc/prometheus-stack-kube-prom-prometheus 9090:9090
Query: up{job="status-page"} in UI for app health.

### Grafana Dashboard
kubectl port-forward -n monitoring svc/prometheus-stack-grafana 3000:80
Login: admin / [your password] | Import grafana-status-dashboard.json for uptime/scrape graphs.

### Jenkins CI/CD
Pipeline: Lint Helm, test template, deploy on main push.
Trigger: GitHub webhook (ngrok tunnel for local).
Test: Push to main → Auto-build → Deploy status-page.

### Challenges
- Metrics "no data": Narrowed time range to 5m; triggered synthetic loads.
- Pipeline "command not found": Bootstrapped tools in stage for ephemeral agents.
- Webhook "received but no trigger": Registered repo in global config; enabled hook trigger.

## Run a Demo
git clone https://github.com/digital-knife/demos.git -b jenkins-integration
cd demos/helm-projects && ./get_helm.sh
