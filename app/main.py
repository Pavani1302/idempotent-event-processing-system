from fastapi import FastAPI

app = FastAPI(
    title = "Idempotent Event Processing System",
    description = "A reliable event processing backend",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "message" : "Idempotent Event Processing System is running"
    }

@app.get("/health")
def health_check():
    return {
        "status" : "healthy"
    }