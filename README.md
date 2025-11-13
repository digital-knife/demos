## Projects

### [AWS Infrastructure Automation](https://github.com/digital-knife/aws-infrastructure)
Multi-environment AWS infrastructure using Terraform, Terragrunt, and Jenkins automation workflows.

**Highlights:**
- 3-tier VPC architecture with network isolation
- Multi-environment management (dev/prod)
- Remote state backend with encryption and locking
- Security-first design (IAM roles, security groups, SSM)
- Cost-optimized S3 lifecycle policies

**Stack**: Terraform 1.9.5 | Terragrunt 0.93.4 | AWS | Jenkins

---

### [Kubernetes Status Page](https://github.com/digital-knife/k8s-status-page)
Helm-deployed application with Prometheus monitoring, Grafana dashboards, and automated CI/CD.

**Highlights:**
- Automated CI/CD pipeline (Git → Jenkins → K8s)
- Prometheus metrics collection
- Grafana visualization dashboards
- Health monitoring and alerting
- Declarative Helm deployments

**Stack**: Kubernetes | Helm 3.x | Prometheus | Grafana | Jenkins

---

### [Healthcheck API](https://github.com/digital-knife/healthcheck-app)
Python REST API with health check endpoints and Ansible-based deployment automation.

**Stack**: Python | Ansible | Flask

---

## Tech Used

| Category | Tools & Platforms |
|----------|-------------------|
| **Cloud** | AWS (VPC, EC2, S3, IAM, DynamoDB) |
| **IaC** | Terraform, Terragrunt |
| **Containers** | Kubernetes, Helm, Docker |
| **CI/CD** | Jenkins (Kubernetes agents) |
| **Monitoring** | Prometheus, Grafana, CloudWatch |
| **Config Mgmt** | Ansible |
| **Languages** | Python, Bash, HCL, YAML |

## Repository Structure

Each project is maintained in its own repository for:
- ✅ Independent CI/CD pipelines and versioning
- ✅ Clear separation of concerns
- ✅ Granular access control
- ✅ Isolated testing and deployment

## What's happening 

**Infrastructure as Code:**
- Terraform modules and state management
- Terragrunt DRY configurations
- Multi-environment deployments

**Cloud Architecture:**
- 3-tier VPC design with security zones
- IAM least-privilege access policies
- Cost optimization strategies

**Container Orchestration:**
- Kubernetes deployments and services
- Helm chart development
- Resource management and scaling

**CI/CD & Automation:**
- Jenkins pipeline development
- GitHub webhook integration
- Automated testing and validation
- Deployment approval workflows

**Monitoring & Observability:**
- Prometheus metrics collection
- Grafana dashboard creation
- Application health monitoring

**Security:**
- Network segmentation
- Encrypted storage (S3, state files)
- Secret management
- Security group configurations

