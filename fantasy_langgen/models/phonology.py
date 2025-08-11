from typing import List
from pydantic import BaseModel, Field, field_validator, model_validator


class ConsonantConstraints(BaseModel):
    initial_clusters: List[str] = Field(default_factory=list)
    forbidden_clusters: List[str] = Field(default_factory=list)


class ConsonantInventory(BaseModel):
    stops: List[str]
    fricatives: List[str]
    nasals: List[str]
    liquids: List[str]
    constraints: ConsonantConstraints = Field(default_factory=ConsonantConstraints)  # noqa:E501

    @field_validator("stops", "fricatives", "nasals", "liquids")
    def validate_phonemes(cls, v):
        for phoneme in v:
            if not phoneme.isalpha() or not phoneme.islower():
                raise ValueError(f"Invalid phoneme: {phoneme}. Must be lowercase letters")
            return v

    @model_validator(mode="after")
    def validate_clusters(self):
        for cluster in self.constraints.get("initial_clusters", []):
            if not all(c in self.stops + self.fricatives + self.nasals + self.liquids for c in cluster):
                raise ValueError(f"Invalid cluster '{cluster}' contains non-consonants")
        return self


class VowelInventory(BaseModel):
    short: List[str]
    long: List[str] = Field(default_factory=list)
    diphthongs: List[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_vowels(self):
        if any(len(v) > 1 for v in self.short):
            raise ValueError("Short vowels must be a single characters")
        return self


class SyllableStructure(BaseModel):
    structure: str = Field(default="CV", pattern=r"^[CV()]+$")
    stress_pattern: str = Field(
        default="penultimate",
        pattern="^(initial|penultimate|ultimate|none)$"
    )


class Phonotactics(BaseModel):
    max_initial_consonants: int = Field(default=1, ge=0)
    max_final_consonants: int = Field(default=1, ge=0)
    vowel_harmony: bool = False


class Phonology(BaseModel):
    consonants: ConsonantInventory
    vowels: VowelInventory
    syllable: SyllableStructure = Field(default_factory=SyllableStructure)
    phonotactics: Phonotactics = Field(default_factory=Phonotactics)
