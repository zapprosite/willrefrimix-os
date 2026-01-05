from fastapi import FastAPI

app = FastAPI(title="Antigravity OS API", version="2.1")

@app.get("/")
async def root():
    return {"status": "online", "system": "Antigravity OS", "engine": "RTX 4090"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
