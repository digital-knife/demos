from fastapi import FastAPI
import os
import platform
import socket
import subprocess
import psutil
from datetime import datetime

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SRE Lab Demo API running!"}


@app.get("/info")
def system_info():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "release": platform.release(),
        "uptime": subprocess.getoutput("uptime -p"),
        "container": os.environ.get("CONTAINER", "false"),
    }


@app.get("/health")
def health_check():
    """Simple health endpoint to verify service responsiveness."""
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.get("/metrics")
def metrics():
    """Expose lightweight system metrics (Prometheus-style)."""
    uptime = subprocess.getoutput("uptime -p")
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()

    return {
        "cpu_percent": cpu_percent,
        "memory_total": mem.total,
        "memory_used": mem.used,
        "memory_percent": mem.percent,
        "uptime": uptime,
    }


@app.get("/version")
def version():
    """Return image version and build timestamp (for CI/CD visibility)."""
    image_tag = os.environ.get("IMAGE_TAG", "unknown")
    build_time = os.environ.get("BUILD_TIME", "not set")
    return {"image_tag": image_tag, "build_time": build_time}
