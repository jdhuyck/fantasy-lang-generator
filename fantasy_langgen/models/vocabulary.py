from typing import Dict, Optional
from pydantic import Field, BaseModel


class WordFormationRules(BaseModel):
    diminutive: Optional[str] = None
    augmentative: Optional[str] = None
    material: Optional[str] = None


class Vocabulary(BaseModel):
    base_words: Dict[str, str] = Field(default_factory=dict)
    word_formation_rules: WordFormationRules = Field(default_factory=WordFormationRules)  # noqa:E501
    semantic_fields: Dict[str, Dict[str, str]] = Field(default_factory=dict)
