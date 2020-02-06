import json
from pathlib import Path

from ward import test

from fact_sphere.models import (
	Audio,
	Fact,
)
from fact_sphere.types import FactType

FILES_DIR = (Path(__file__).parent / 'files').resolve()
FACT_FILE = FILES_DIR / 'fact.json'
AUDIO_FILE = FILES_DIR / 'true_01.wav'
FACT_DATA = json.loads(FACT_FILE.read_text())


@test("Test models.")
def _():
	fact = Fact(
		text=FACT_DATA['text'],
		audio=FILES_DIR / FACT_DATA['audio'],
		type=FACT_DATA['type']
	)
	audio = Audio(AUDIO_FILE)

	assert fact.text == "The billionth digit of Pi is 9."
	assert fact.type is FactType.TRUE
	assert fact.audio == audio

	assert audio.filepath == AUDIO_FILE
	assert audio.read() == AUDIO_FILE.read_bytes()
