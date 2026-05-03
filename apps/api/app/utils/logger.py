import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

_handler = TimedRotatingFileHandler(
    filename=f"logs/{datetime.utcnow().strftime('%Y-%m-%d')}.log",
    when="midnight", interval=1, backupCount=30, utc=True,
)
_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"))


def get_logger() -> logging.Logger:
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(_handler)
    return logger


logger = get_logger()
