__all__ = ["ActivityWatchClient"]

def __getattr__(name: str):
	"""Lazy import attributes to avoid heavy imports on package import.

	Accessing `aw_client.ActivityWatchClient` will import it on demand.
	"""
	if name == "ActivityWatchClient":
		from .client import ActivityWatchClient

		return ActivityWatchClient
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
