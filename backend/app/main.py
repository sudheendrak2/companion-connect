from fastapi import FastAPI

app = FastAPI(title="Companion Connect API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Used by CI, load balancers, and uptime checks."""
    return {"status": "ok"}
