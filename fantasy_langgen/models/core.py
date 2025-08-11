from datetime import datetime, timezone
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, field_validator, model_validator
from .phonology import Phonology
from .vocabulary import Vocabulary
from .grammar import Grammar
from .culture import CulturalInfluences


class VersionHistory(BaseModel):
    version: int = Field(..., gt=0)
    modified_at: datetime
    modified_by: str
    changeset: Optional[str] = None


class LanguageMetadata(BaseModel):
    language_name: str
    creator: str
    created_at: datetime
    last_modified: datetime
    version: int
    description: Optional[str] = None
    tags: List[str]

    # Versioning fields
    parent_id: Optional[str] = None
    original_creator: Optional[str] = None
    version_history: List[VersionHistory]

    @field_validator("language_name")
    def validate_name(cls, v):
        if not v[0].isupper():
            raise ValueError("Language name must start with uppercase letter")
        return v
    
    @field_validator("version")
    def validate_version(cls, v):
        if v <= 0:
            raise ValueError("Version must be positive")
        return v


class DerivedContent(BaseModel):
    generated_words: List[Dict[str, object]] = Field(default_factory=list)
    sample_sentence: List[Dict[str, str]] = Field(default_factory=list)
    generation_parameters: Dict[str, object]


class Language(BaseModel):
    metadata: LanguageMetadata
    phonology: Phonology
    vocabulary: Vocabulary
    grammar: Grammar
    cultural_influences: CulturalInfluences
    derived_content: DerivedContent

    @model_validator(mode="after")
    def validate_language(self):
        for word in self.vocabulary.base_words.values():
            if not all(c in self.phonology.get_all_phonemes() for c in word):
                raise ValueError(f"Word '{word}' contains invalid phonemes")

        if "plural" in self.grammar.noun:
            for form in self.grammar.noun["plural_forms"]:
                if form["suffix"] not in self.vocabulary.word_formation_rules.values():
                    raise ValueError(f"Plural suffix {form["suffix"]} not in word formation rules")

        return self
