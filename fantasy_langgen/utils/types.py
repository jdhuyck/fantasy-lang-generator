from typing import NewType, Literal, TypedDict
from datetime import datetime
from pydantic import confloat, conint


# Phonetic Types
Phoneme = NewType("Phoneme", str)
Consonant = NewType("Consonant", Phoneme)
Vowel = NewType("Vowel", Phoneme)
SyllablePattern = NewType("SyllablePattern", str)

# Validation Types
ISO8601DateTime = NewType("ISO8601DateTime", datetime)
ConfidenceScore = confloat(ge=0.0, le=1.0)
TechLevel = conint(ge=1, le=10)


# Structure Types
class WordComponents(TypedDict):
    root: str
    affixes: list[str]
    phonetic_breakdown: list[Phoneme]


class GeneratedSentence(TypedDict):
    text: str
    translation: str
    structure: dict
    word_analysis: list[WordComponents]


# Enums
WordOrder = Literal["SOV", "SVO", "VSO", "VOS", "OVS", "OSV"]
EnvironmentType = Literal[
    "mountainous", "forest", "desert", "coastal", "urban", "underground"
]
SocialStructure = Literal[
    "clan_hierarchy", "egalitarian", "matriarchal", "imperial", "tribal"
]
StressPattern = Literal["initial", "penultimate", "ultimate", "none"]


class GenerationConstraints(TypedDict, total=False):
    min_syllables: conint(ge=1, le=5)
    max_syllables: conint(ge=1, le=5)
    semantic_field: str
    allow_borrowing: bool
    complexity: Literal["simple", "medium", "complex"]


class VersionChange(TypedDict):
    path: str
    operation: Literal["add", "remove", "modify"]
    old_value: object | None
    new_value: object | None
