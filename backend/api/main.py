from fastapi import FastAPI

app = FastAPI(
    title="SyncReserve AI API",
    description="Backend API for the SyncReserve AI project.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to SyncReserve AI Backend"
    }