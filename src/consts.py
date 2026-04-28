try:
	from .ankiutils.consts import get_consts
except ImportError:  # pragma: no cover
	from ankiutils.consts import get_consts

consts = get_consts(__name__)
