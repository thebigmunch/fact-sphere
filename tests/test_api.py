from ward import test

import fact_sphere
from fact_sphere.facts import FACTS_DIR
from fact_sphere.models import (
	Audio,
	Fact
)
from fact_sphere.types import FactType

AUDIO_FILEPATHS = list((FACTS_DIR / 'audio').iterdir())


@test("Test fact_sphere.audio.")
def _():
	audio = fact_sphere.audio()

	assert isinstance(audio, Audio)
	assert audio.filepath in AUDIO_FILEPATHS


@test("Test fact_sphere.fact.")
def _():
	fact = fact_sphere.fact()

	assert isinstance(fact, Fact)

	fact = fact_sphere.fact(fact_type=FactType.TRUE)

	assert isinstance(fact, Fact)
	assert fact.type is FactType.TRUE

	fact = fact_sphere.fact(fact_type=FactType.FALSE)

	assert isinstance(fact, Fact)
	assert fact.type is FactType.FALSE

	fact = fact_sphere.fact(fact_type=None)

	assert isinstance(fact, Fact)
	assert fact.type in FactType


@test("Test fact_sphere.text.")
def _():
	text = fact_sphere.text()

	assert isinstance(text, str)
