from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Receipt Processor", description="A simple receipt processor", version="1.0.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
