# DevSecOps & Cloud-Native CI/CD Pipeline Capstone

[![DevSecOps CI/CD Pipeline](https://github.com/dez84/devops-cicd-capstone/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/dez84/devops-cicd-capstone/actions/workflows/ci-cd.yml)
[![Docker Image](https://img.shields.io/badge/Container%20Registry-GHCR-blue.svg)](https://github.com/dez84/devops-cicd-capstone/pkgs/container/devops-cicd-capstone)
[![Python Version](https://img.shields.io/badge/Python-3.11-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-grade DevSecOps capstone project demonstrating automated continuous integration, unit testing, containerization, and publishing to GitHub Container Registry (`ghcr.io`) using GitHub Actions.

---

## 🏛️ System Architecture & Workflow

```text
  +------------------+         +--------------------+         +-----------------------+
  |  Local Dev (WSL) |         |   GitHub Actions   |         |   GitHub Container    |
  |  FastAPI / Pytest| ------->|   CI/CD Pipeline   | ------->|   Registry (ghcr.io)  |
  +------------------+  Push   +--------------------+  Publish+-----------------------+
                                 | Unit Tests       |
                                 | Image Build      |
                                 | Vulnerability Check|

## 🛠️ Tech Stack & Tooling

| Domain | Technology / Tool |
| :--- | :--- |
| **Language & Framework** | Python 3.11, FastAPI, Uvicorn |
| **Testing Framework** | Pytest, HTTPX, Starlette TestClient |
| **Containerization** | Docker, OCI Image Specs, Python-slim Base |
| **CI/CD Automation** | GitHub Actions Workflow (`ci-cd.yml`) |
| **Artifact Storage** | GitHub Container Registry (`ghcr.io`) |
| **Environment** | Linux (Ubuntu / WSL2), Bash |

---

## 🚀 Quick Start Guide

### 1. Run via Docker Container (Recommended)

Pull and run the pre-built, production-ready container image directly from GitHub Container Registry:

```bash
# Pull image from GHCR
docker pull ghcr.io/dez84/devops-cicd-capstone:latest

# Run container on port 8000
docker run -d -p 8000:8000 --name capstone-app ghcr.io/dez84/devops-cicd-capstone:latest

# Verify service health
curl http://localhost:8000/
curl http://localhost:8000/health

2. Local Development & Setup (WSL / Linux)

# Clone the repository
git clone [https://github.com/dez84/devops-cicd-capstone.git](https://github.com/dez84/devops-cicd-capstone.git)
cd devops-cicd-capstone

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run test suite
python -m pytest

# Run application server locally
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## 🧪 API Endpoints & Health Checks

| Endpoint | Method | Response Example | Description |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | `{"status":"healthy","service":"devops-capstone-api"}` | Root API health status check |
| `/health` | `GET` | `{"status":"UP"}` | Liveness / Readiness probe endpoint |
| `/docs` | `GET` | *Swagger UI Page* | Interactive API Documentation |

---

## ⚙️ CI/CD Pipeline Breakdown

The workflow in `.github/workflows/ci-cd.yml` automates the release process:

- **`test` Job**:
  - Provisions `ubuntu-latest` runner with Python 3.11.
  - Caches `pip` dependencies for optimized build times.
  - Executes unit test suite with strict pass/fail status checks.

- **`build-and-push` Job**:
  - Dependent on successful `test` execution (`needs: test`).
  - Authenticates with `ghcr.io` via `GITHUB_TOKEN`.
  - Generates short Git SHA tags (`type=sha`) and `latest` tags.
  - Pushes production OCI image to container registry.

---

## 👤 Author & Maintainer

**Desmoine "Dez" Smith**
- **GitHub**: [@dez84](https://github.com/dez84)
- **Specializations**: DevSecOps, Site Reliability Engineering (SRE), Cloud Infrastructure, Data Analytics & Governance
- **Certifications**: ISO/IEC 27001 Lead Auditor

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

