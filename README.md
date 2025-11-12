## 📚 Projects

### **AWS Infrastructure (Terraform/Terragrunt)**
3-tier VPC architecture with multi-environment management, remote state backend (S3+DynamoDB), and Jenkins automation.

**Stack**: Terraform 1.9.5 | Terragrunt 0.93.4 | Jenkins on Kubernetes | AWS

### **Kubernetes (Helm)**
Status page application with Prometheus monitoring, Grafana dashboards, and automated CI/CD.

**Stack**: Kubernetes | Helm 3.x | Prometheus | Grafana

### **Other Demos**
- **Healthcheck App**: Python API with Ansible deployment
- **Postman Tests**: API testing collections

---

## 🚀 Quick Start

### AWS Infrastructure
```bash
git clone https://github.com/digital-knife/demos.git
cd demos/cloud-projects

# Bootstrap state backend (one-time)
cd terraform-state-backend
terraform init && terraform apply

# Deploy via Terragrunt
cd ../dev
terragrunt init && terragrunt apply
```

**OR** use Jenkins automation workflow with parameter-driven deployment (region, VPC CIDR, instance types).

### Kubernetes Status Page
```bash
git clone https://github.com/digital-knife/demos.git -b jenkins-integration
cd demos/helm-projects

# Setup
./get_helm.sh
minikube start --driver=docker

# Deploy
helm install status-page ./status-page --set service.type=NodePort
minikube service status-page --url

# Monitoring
helm install prometheus-stack prometheus-community/kube-prometheus-stack \
  -f prometheus-custom-values.yaml --namespace monitoring --create-namespace

kubectl port-forward -n monitoring svc/prometheus-stack-grafana 3000:80
# Login: admin / [password from secret]
# Import: grafana-status-dashboard.json
```

---

## 🏗️ Architecture

### AWS Infrastructure (3-Tier)
```
Internet → IGW → Public Subnet (Bastion + NAT)
                      ↓
             Private Subnets (Web + App Tiers)
```

**Components:**
- VPC with isolated dev (10.0.0.0/16) and prod (10.1.0.0/16) environments
- 3 EC2 instances (bastion, web, app) with tier-based security groups
- S3 bucket with encryption, versioning, lifecycle policies (30d→IA, 90d→Glacier)
- IAM roles with least-privilege access
- Remote state: S3 + DynamoDB locking

**Security:**
- Bastion: SSH from allowed CIDR only
- Web: HTTP/HTTPS + SSH from bastion
- App: Port 8080 from web tier + SSH from bastion

---

## 📁 Project Structure
```
demos/
├── cloud-projects/              # Terraform/Terragrunt
│   ├── terraform-state-backend/ # S3 + DynamoDB bootstrap
│   ├── dev/                     # Dev environment
│   ├── prod/                    # Prod environment
│   ├── *.tf                     # Infrastructure modules
│   ├── Jenkinsfile              # Automation workflow
│   └── root.hcl                 # Terragrunt config
├── helm-projects/               # Kubernetes apps
│   ├── status-page/             # Helm chart
│   ├── prometheus-custom-values.yaml
│   └── grafana-status-dashboard.json
├── healthcheck-app/             # Python API
└── postman-tests/               # API tests
```

---

## 🤖 Automation Workflows

### Terraform Infrastructure Deployment (Jenkins)
Parameterized Jenkins job for AWS infrastructure provisioning with Terragrunt.

**Flow**: Validate → Init → Plan → Approval → Apply → Validate → Archive

**Features:**
- Parameter-driven (region, CIDR, instance types)
- Environment-locked CIDR validation
- Manual approval gates
- Auto-cleanup on failure
- State artifact archiving

### Application CI/CD Pipeline (Jenkins)
Automated Helm deployment triggered by Git push to main branch.
**Flow**: Lint → Test → Deploy
**Trigger**: GitHub webhook (ngrok for local testing)

---

## 🛠️ Key Technologies

| Category | Tools |
|----------|-------|
| **IaC** | Terraform, Terragrunt |
| **Cloud** | AWS (VPC, EC2, S3, IAM, DynamoDB) |
| **Containers** | Kubernetes, Helm, Docker |
| **CI/CD** | Jenkins (K8s agents), GitHub webhooks |
| **Monitoring** | Prometheus, Grafana, CloudWatch |
| **Config Mgmt** | Ansible, Python |

---

## 📋 Prerequisites

**AWS Infrastructure:**
- AWS account with appropriate permissions
- Jenkins with Kubernetes plugin + AWS credentials

**Kubernetes:**
- Docker + Minikube (or K8s cluster)
- kubectl + Helm 3.x

---

## 🧪 Testing

- **Infrastructure**: Terraform plan validation, CIDR validation, post-deploy checks
- **Application**: Helm linting, template validation, health endpoint tests

---
## 👤 Author

**digital-knife** - [@digital-knife](https://github.com/digital-knife)
