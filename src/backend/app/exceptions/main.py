import logging

from fastapi import FastAPI

from app.exceptions.base import BaseAppException

from app.exceptions.error_handlers import application_exception_handler

logger = logging.getLogger(__name__)


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(BaseAppException, application_exception_handler)  # type: ignore
    logger.info("Setup %s error handler", BaseAppException)
