__all__ = ['Audio', 'Fact']

from pathlib import Path

from attr import attrib, attrs

from .types import FactType


@attrs
class Audio:
	"""A representation of fact audio.

	Attributes:
		filepath (str): The filepath to the fact audio.
	"""

	filepath = attrib(converter=lambda f: Path(f).resolve())

	def read(self):
		"""Get the binary data from the fact audio file."""

		with open(self.filepath, 'rb') as f:
			return f.read()


@attrs
class Fact:
	"""A representation of a fact.

	Attributes:
		audio (Audio): The fact audio.
		text (str): The fact text.
		type (FactType): The fact type.
	"""

	text = attrib()
	audio = attrib(
		converter=lambda a: Audio(a) if not isinstance(a, Audio) else a
	)
	type = attrib(  # noqa
		converter=lambda t: FactType[t] if not isinstance(t, FactType) else t
	)
