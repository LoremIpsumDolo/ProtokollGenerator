import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler
from rich.traceback import install

from app.classes.config import Config

from pathlib import Path
from datetime import datetime
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)


def make_logger():
	log_name = str(datetime.now().date())
	path = f"app/logs/{log_name}.log"
	Path('app/logs/').mkdir(parents=True, exist_ok=True)

	install(show_locals=True)
	logger = logging.getLogger(__name__)

	debug_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
	file_handler = RotatingFileHandler(path,
	                                   maxBytes=1000000,
	                                   backupCount=3)

	file_handler.setFormatter(debug_formatter)
	logger.addHandler(file_handler)
	logger.addHandler(RichHandler(rich_tracebacks=True))
	logger.setLevel(logging.DEBUG)
	return logger


logger = make_logger()
config = Config()
