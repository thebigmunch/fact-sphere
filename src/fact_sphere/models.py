__all__ = ['Audio', 'Fact']

from attr import attrib, attrs


@attrs
class Audio:
	"""A representation of fact audio.

	Attributes:
		filepath (str): The filepath to the fact audio.
	"""

	filepath = attrib()

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
	audio = attrib(converter=Audio)
	type = attrib()  # noqa
