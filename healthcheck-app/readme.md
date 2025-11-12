# SRE Lab Demo

A minimal FastAPI app for practicing SRE fundamentals — Python, Docker, and Ansible.

## Run locally
```bash
python3 -m venv .venv-sre-lab
source .venv-sre-lab/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload

