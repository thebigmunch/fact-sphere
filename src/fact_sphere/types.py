__all__ = ['FactType']

from enum import Enum


class FactType(Enum):
	TRUE = "True Facts"
	NEARLY_TRUE = "Nearly True Facts"
	PARTIALLY_TRUE = "Partially True Facts"
	PROBABLY_FALSE = "Probably False Facts"
	FALSE = "False Facts"
	SUBJECTIVE_UNVERIFIABLE = "Subjective or Unverifiable Facts"
	NOT_FACTS = "Not Facts"
