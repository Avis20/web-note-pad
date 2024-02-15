from logging import config as logging_config
from app.exceptions.main import setup_error_handlers

from app.logger import LOGGING
from app.routers.main import setup_routers
from app.settings import Settings
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.project.name,
        debug=settings.project.debug,
        docs_url="/docs",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
        description="Web Notepad",
        version="1.0.0",
    )
    # setup_dependencies(app)
    # setup_providers(app, settings)
    setup_routers(app)
    # setup_middleware(app)
    # setup_telemetry(app, settings)
    setup_error_handlers(app)
    return app


logging_config.dictConfig(LOGGING)
settings = Settings()
app = create_app(settings)
