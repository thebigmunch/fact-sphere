__all__ = ['FACTS', 'TYPE_FACTS']

import json
import os

from ..models import Fact
from ..types import FactType


TYPE_FACTS = {fact_type: [] for fact_type in FactType}
FACTS = []

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, 'facts.json'), 'r') as f:
	facts = json.load(f)

	for type_, type_facts in facts.items():
		for fct in type_facts:
			fact = Fact(fct['text'], os.path.join(dirname, 'audio', fct['audio']), FactType[type_])
			FACTS.append(fact)
			TYPE_FACTS[FactType[type_]].append(fact)
