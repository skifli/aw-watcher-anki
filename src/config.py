try:
	from .ankiutils.config import Config
except ImportError:  # pragma: no cover
	from ankiutils.config import Config

config = Config(__name__)
