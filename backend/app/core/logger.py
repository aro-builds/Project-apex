from loguru import logger

logger.add(
    "logs/backend.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
)

__all__ = ["logger"]