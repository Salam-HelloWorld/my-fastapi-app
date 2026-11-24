from fastapi import FastAPI

from app.routers import items
from app.config import get_settings

tags_metadata = [
    {"name": "meta", "description": "Service info and health checks."},
    {"name": "items", "description": "Create, read, update and delete items (stored in memory)."},
]

app = FastAPI(
    title="Simple Backend Example",
    description="A minimal FastAPI backend with in-memory storage (no database).",
    version="0.1.0",
    openapi_tags=tags_metadata,
    docs_url="/docs",            # Swagger UI
    redoc_url="/redoc",          # ReDoc (alternative docs)
    openapi_url="/openapi.json", # Raw OpenAPI schema
    swagger_ui_parameters={
        "docExpansion": "list",
        "defaultModelsExpandDepth": 1,
        "tryItOutEnabled": True,
        "displayRequestDuration": True,
    },
)

app.include_router(items.router)


@app.get("/", tags=["meta"])
def root() -> dict[str, str]:
    settings = get_settings()
    return {"message": settings.welcome_message, "docs": "/docs"}


@app.get("/config", tags=["meta"])
def config() -> dict[str, str | bool]:
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "app_env": settings.app_env,
        "app_version": settings.app_version,
        "welcome_message": settings.welcome_message,
        "api_secret_configured": bool(settings.api_secret),
    }


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
        raise Exception("broken on purpose")
