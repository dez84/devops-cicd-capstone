from fastapi import FastAPI

app = FastAPI(title="DevOps DevSecOps Capstone API")

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "devops-capstone-api"}

@app.get("/health")
def health_check():
    return {"status": "UP"}