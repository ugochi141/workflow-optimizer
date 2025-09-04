from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up workflow-optimizer...")
    yield
    logger.info("Shutting down workflow-optimizer...")

app = FastAPI(
    title="workflow-optimizer",
    description="Process mining and optimization system for laboratory workflow improvement",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "project": "workflow-optimizer",
        "status": "operational",
        "description": "Process mining and optimization system for laboratory workflow improvement"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/status")
async def api_status():
    return {
        "api_version": "v1",
        "status": "operational",
        "endpoints_available": True
    }
