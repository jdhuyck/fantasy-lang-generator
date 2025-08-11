from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class PluralForm(BaseModel):
    pattern: str
    suffix: Optional[str] = None
    exceptions: Dict[str, str] = Field(default_factory=dict)


class NounGrammar(BaseModel):
    cases: List[str] = Field(default_factory=list)
    genders: List[str] = Field(default_factory=list)
    plural_forms: List[PluralForm] = Field(default_factory=list)


class VerbConjugation(BaseModel):
    parent: str
    past: Optional[str] = None
    future: Optional[str] = None


class VerbGrammar(BaseModel):
    tenses: List[str] = Field(default_factory=list)
    conjugation_patterns: Dict[str, Dict[str, str]] = Field(default_factory=dict)  # noqa:E501


class AdjectiveGrammar(BaseModel):
    position: str = Field(default="prenominal", regex="^(prenominal|postnominal)$")  # noqa:E501
    comparative: Optional[str] = None
    superlative: Optional[str] = None


class Grammar(BaseModel):
    word_order: str = Field(
        default="SOV",
        regex="^(SOV|SVO|VSO|VOS|OVS|OSV)$"
    )
    noun: NounGrammar = Field(default_factory=NounGrammar)
    verb: VerbGrammar = Field(default_factory=VerbGrammar)
    adjectives: AdjectiveGrammar = Field(default_factory=AdjectiveGrammar)
