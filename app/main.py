from fastapi import FastAPI

app = FastAPI(
    title="Portfolio Risk Analytics API",
    description="Analyze historical portfolio performance and risk.",
    version="0.1.0",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "running"}