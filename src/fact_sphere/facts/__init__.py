__all__ = ['FACTS', 'TYPE_FACTS']

import json
from pathlib import Path

from ..models import Fact
from ..types import FactType


TYPE_FACTS = {fact_type: [] for fact_type in FactType}
FACTS = []

FACTS_DIR = Path(__file__).parent.resolve()
FACTS_FILE = FACTS_DIR / 'facts.json'


facts = json.loads(FACTS_FILE.read_text())

for type_, type_facts in facts.items():
	for fct in type_facts:
		fact = Fact(
			fct['text'],
			FACTS_DIR / 'audio' / fct['audio'],
			FactType[type_],
		)
		FACTS.append(fact)
		TYPE_FACTS[FactType[type_]].append(fact)
