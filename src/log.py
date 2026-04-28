try:
	from .ankiutils.log import get_logger
except ImportError:  # pragma: no cover
	from ankiutils.log import get_logger

logger = get_logger(__name__)
