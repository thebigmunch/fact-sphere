__all__ = ['audio', 'fact', 'text']

import random

from .facts import FACTS, TYPE_FACTS
from .types import FactType


def audio(fact_type=None):
	"""Get the audio for a random fact.

	Parameters:
		fact_type (FactType): The type of fact to return.
			Default: Get any type of fact.

	Returns:
		Audio: An audio object.
	"""

	return fact(fact_type=fact_type).audio


def fact(fact_type=None):
	"""Get the audio filepath, text and fact type for a random fact.

	Parameters:
		fact_type (FactType): The type of fact to return.
			Default: Get any type of fact.

	Returns:
		Fact: A fact object.
	"""

	if fact_type in FactType:
		return random.choice(TYPE_FACTS[fact_type])

	return random.choice(FACTS)


def text(fact_type=None):
	"""Get the text for a random fact.

	Parameters:
		fact_type (FactType): The type of fact to return.
			Default: Get any type of fact.

	Returns:
		str: The fact text.
	"""

	return fact(fact_type=fact_type).text
