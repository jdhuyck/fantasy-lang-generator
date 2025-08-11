from typing import List
from pydantic import BaseModel, Field


class ConsonantConstraints(BaseModel):
    initial_clusters: List[str] = Field(default_factory=list)
    forbidden_clusters: List[str] = Field(default_factory=list)


class ConsonantInventory(BaseModel):
    stops: List[str]
    fricatives: List[str]
    nasals: List[str]
    liquids: List[str]
    constraints: ConsonantConstraints = Field(default_factory=ConsonantConstraints)  # noqa:E501


class VowelInventory(BaseModel):
    short: List[str]
    long: List[str] = Field(default_factory=list)
    diphthongs: List[str] = Field(default_factory=list)


class SyllableStructure(BaseModel):
    structure: str = Field(default="CV", regex=r"^[CV()]+$")
    stress_pattern: str = Field(
        default="penultimate",
        regex="^(initial|penultimate|ultimate|none)$"
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
