# Use a lightweight but functional Python base
FROM python:3.11-slim

# Ensure non-interactive and consistent builds
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Update apt and install dependencies properly
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        curl \
        procps \
        bash \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency list and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Build metadata (optional)
ARG IMAGE_TAG=local
ARG BUILD_TIME=unknown
ENV IMAGE_TAG=${IMAGE_TAG}
ENV BUILD_TIME=${BUILD_TIME}

# Run FastAPI app — note the correct module path here
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
